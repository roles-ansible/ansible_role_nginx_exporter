Ansible Role Nginx Exporter
=========

Ansible role to install Nginx Prometheus Exporter

Requirements
------------

None

Role Variables
--------------

| variable                      | default                           | comment                       |
|-------------------------------|-----------------------------------|-------------------------------|
| nginx_exporter_version        | 0.3.0                             | nginx exporter version        |
| nginx_exporter_nginx_plus     | false                             | set true if use nginx plus    |
| nginx_exporter_listen_address | 0.0.0.0:9113                      | nginx exporter listen address |
| nginx_exporter_scrape_uri     | http://127.0.0.1:8080/stub_status | nginx status url              |

Dependencies
------------

geerlingguy.nginx

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
        - geerlingguy.nginx
        - cloudweeb.nginx_exporter

License
-------

MIT / BSD

Author Information
------------------

Agnesius Santo Naibaho
