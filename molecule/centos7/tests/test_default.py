import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_apache_running_and_enabled(host):
    apache = host.service("httpd24-httpd")

    assert apache.is_running
    assert apache.is_enabled


def test_apache_network(host):
    assert host.socket("tcp://127.0.0.1:8080").is_listening
    assert host.socket("tcp://127.0.0.1:8443").is_listening
