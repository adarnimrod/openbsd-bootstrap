def test_example(Command):
    assert Command('uname').rc == 0


def test_ansible(Ansible):
    assert Ansible('debug', 'msg={{ eleven }}')['msg'] == '11'
