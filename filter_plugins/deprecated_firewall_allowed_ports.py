#!/bin/bash
from ansible.utils.display import Display

display = Display()

# Warnings to advise using firewall_*_ports rather than firewall_*_allowed_ports
# They propagate the value of firewall_*_allowed_ports after warning
def warn_tcp(tcp_allowed_ports):
    if tcp_allowed_ports != []:
        display.warning('Variable "firewall_tcp_allowed_ports" has been superseded by "firewall_tcp_ports".')

    return tcp_allowed_ports

def warn_udp(udp_allowed_ports):
    if udp_allowed_ports != []:
        display.warning('Variable "firewall_udp_allowed_ports" has been superseded by "firewall_udp_ports".')

    return udp_allowed_ports


class FilterModule(object):
    def filters(self):
        return {
            "warn_tcp": warn_tcp,
            "warn_udp": warn_udp
        }
