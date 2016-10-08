def test_example(Command):
    assert Command('uname').rc == 0


def test_root(Command, Sudo):
    with Sudo():
        assert Command('whoami').stdout == 'root'
