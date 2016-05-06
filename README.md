# Ansible Role: Firewall (iptables)

[![Build Status](https://travis-ci.org/geerlingguy/ansible-role-firewall.svg?branch=master)](https://travis-ci.org/geerlingguy/ansible-role-firewall)

Installs a simple iptables-based firewall for RHEL/CentOS or Debian/Ubunty systems.

This firewall aims for simplicity over complexity, and only opens a few specific ports for incoming traffic (configurable through Ansible variables). If you have a rudimentary knowledge of `iptables` and/or firewalls in general, this role should be a good starting point for a secure system firewall.

After the role is run, a `firewall` init service will be available on the server. You can use `service firewall [start|stop|restart|status]` to control the firewall.

## Requirements

None.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

    firewall_allowed_tcp_ports:
      - "22"
      - "80"
      ...
    firewall_allowed_udp_ports: []

A list of TCP or UDP ports (respectively) to open to incoming traffic.

    firewall_forwarded_tcp_ports:
      - { src: "22", dest: "2222" }
      - { src: "80", dest: "8080" }
    firewall_forwarded_udp_ports: []

Forward `src` port to `dest` port, either TCP or UDP (respectively).

    firewall_additional_rules: []

Any additional (custom) rules to be added to the firewall (in the same format you would add them via command line, e.g. `iptables [rule]`).

    firewall_log_dropped_packets: true

Whether to log dropped packets to syslog (messages will be prefixed with "Dropped by firewall: ").

    firewall_conditionally_allowed_ports: []

Ports to be opened to particular hosts. Either a source as defined by iptables (network name, a hostname, a network IP address (with /mask), or a plain IP address) or a group of ansible hosts. Ansible hosts will be converted to IP addresses. If protocol is not specified, tcp will be used.

## Dependencies

None.

## Example Playbook

    - hosts: server
      vars_files:
        - vars/main.yml
      roles:
        - { role: geerlingguy.firewall }

*Inside `vars/main.yml`*:

    firewall_allowed_tcp_ports:
      - "22"
      - "25"
      - "80"
    firewall_conditionally_allowed_ports: 
      - sources: ['1.1.2.0/24',  '1.2.2.2']
        ports: [11111, 11000]
        protocol: "udp"
      - ansible_hosts: "{{ groups['all'] }}"
        ports: [22222]
      - ansible_hosts: "{{ groups['aaa'] + groups['bbb'] }}"
        ports: [44444]
        protocol: "udp"
        
## TODO

  - Make outgoing ports more configurable.
  - Make other firewall features (like logging) configurable.

## License

MIT / BSD

## Author Information

This role was created in 2014 by [Jeff Geerling](http://jeffgeerling.com/), author of [Ansible for DevOps](http://ansiblefordevops.com/).
