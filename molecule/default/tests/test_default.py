import pytest
import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


@pytest.mark.parametrize("files", [
    "/usr/local/bin/nginx_exporter",
    "/etc/systemd/system/nginx_exporter.service"
])
def test_files(host, files):
    f = host.file(files)
    assert f.exists
    assert f.is_file


@pytest.mark.parametrize("sockets", [
    "tcp://127.0.0.1:8080",
    "tcp://0.0.0.0:9113"
])
def test_socket(host, sockets):
    s = host.socket(sockets)
    assert s.is_listening
