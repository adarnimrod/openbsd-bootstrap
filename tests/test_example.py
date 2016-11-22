from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_example(Command):
    assert Command('uname').rc == 0


def test_root(Command, Sudo):
    with Sudo():
        assert Command('whoami').stdout.strip() == 'root'
