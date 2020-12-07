import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_apache_running_and_enabled(host):
    apache = host.service("httpd")

    assert apache.is_running
    assert apache.is_enabled
