Ansible Role Nginx Exporter
=========

[![Build Status](https://travis-ci.com/cloudweeb/ansible-role-nginx_exporter.svg?branch=master)](https://travis-ci.com/cloudweeb/ansible-role-nginx_exporter)

Ansible role to install Nginx Prometheus Exporter

Requirements
------------

None

Role Variables
--------------

| variable                      | default                           | comment                       |
|-------------------------------|-----------------------------------|-------------------------------|
| nginx_exporter_version        | 0.9.0                             | nginx exporter version        |
| nginx_exporter_nginx_plus     | false                             | set true if use nginx plus    |
| nginx_exporter_listen_address | 0.0.0.0:9113                      | nginx exporter listen address |
| nginx_exporter_scrape_uri     | <http://127.0.0.1:8080/stub_status> | nginx status url              |

Dependencies
------------

geerlingguy.nginx

Example Playbook
----------------

    - hosts: servers
      vars:
        nginx_vhosts:
          - listen: "127.0.0.1:8080 default"
            server_name: "_"
            filename: "status.conf"
            extra_parameters: |
              location / {
                  stub_status  on;
                  access_log   off;
              }

      roles:
        - geerlingguy.nginx
        - cloudweeb.nginx_exporter

License
-------

MIT / BSD

Author Information
------------------

Agnesius Santo Naibaho
