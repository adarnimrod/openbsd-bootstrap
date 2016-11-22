from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_python(Command):
    python = Command('python --version')
    assert python.rc == 0
    assert '2.7' in python.stderr
