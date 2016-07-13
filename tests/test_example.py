def test_example(Command):
    assert Command('uname').rc == 0
