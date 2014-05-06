# Ansible Role: Firewall (iptables)

Installs a simple iptables-based firewall for RHEL/CentOS or Debian/Ubunty systems.

This firewall aims for simplicity over complexity, and only opens a few specific ports for incoming traffic (configurable through Ansible variables). If you have a rudimentary knowledge of `iptables` and/or firewalls in general, this role should be a good starting point for a secure system firewall.

After the role is run, a `firewall` init service will be available on the server. You can use `service firewall [start|stop|restart|status]` to control the firewall.

## Requirements

None.

## Role Variables

Available variables are listed below, along with default values (see `vars/main.yml`):

    firewall_allowed_tcp_ports:
      - "22"
      - "80"
      ...
    firewall_allowed_udp_ports: []
    firewall_allowed_hosts: []

A list of TCP or UDP ports (respectively) to open to incoming traffic.

    firewall_forwarded_tcp_ports:
      - { src: "22", dest: "2222" }
      - { src: "80", dest: "8080" }
    firewall_forwarded_udp_ports: []

Forward `src` port to `dest` port, either TCP or UDP (respectively).

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
    firewall_allowed_hosts: {{ groups['appservers'] }}
    # here, for example, only your appservers will be able to reach your database ports
    # note: you should still use a password on your database but this adds an another security layer

## TODO

  - Make outgoing ports more configurable.
  - Make other firewall features (like logging) configurable.

## License

MIT / BSD

## Author Information

This role was created in 2014 by [Jeff Geerling](http://jeffgeerling.com/), author of [Ansible for DevOps](http://ansiblefordevops.com/).

Other contributors:

- [Robin Ricard](https://github.com/rricard)
