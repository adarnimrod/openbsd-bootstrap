def test_python(Command):
    assert Command('python --version').rc == 0
