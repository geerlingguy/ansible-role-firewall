import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("rule", [
    ("-A INPUT -p tcp -m tcp --dport 1234 -j ACCEPT"),
    ("-A INPUT -p udp -m udp --dport 5678 -j ACCEPT"),
    ("-A INPUT -s 192.168.1.1/32 -p tcp -m tcp --dport 4949 -j ACCEPT"),
])
def test_filter_rules(host, rule):
    filter_input = host.iptables.rules("filter")
    if host.system_info.distribution.lower() == "centos":
        # fix for trailing slashes in iptables rules output
        filter_input = map(unicode.strip, filter_input) 
    assert rule in filter_input


def test_filter_last_input_drop(host):
    filter_input = host.iptables.rules("filter", "INPUT")
    if host.system_info.distribution.lower() == "centos":
        # fix for trailing slashes in iptables rules output
        filter_input = map(unicode.strip, filter_input) 
    assert filter_input[-1] == "-A INPUT -j DROP"


@pytest.mark.parametrize("rule", [
    ("-A PREROUTING -p udp -m udp --dport 33 -j REDIRECT --to-ports 3333"),
    ("-A PREROUTING -p tcp -m tcp --dport 22 -j REDIRECT --to-ports 2222"),
    ("-A OUTPUT -o lo -p udp -m udp --dport 33 -j REDIRECT --to-ports 3333"),
    ("-A OUTPUT -o lo -p tcp -m tcp --dport 22 -j REDIRECT --to-ports 2222"),
])
def test_nat_rules(host, rule):
    nat = host.iptables.rules("nat")
    if host.system_info.distribution.lower() == "centos":
        # fix for trailing slashes in iptables rules output
        nat = map(unicode.strip, nat) 
    assert rule in nat
