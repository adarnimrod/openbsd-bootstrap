def test_python(Command):
    python = Command('python --version')
    assert python.rc == 0
    assert '2.7' in python.stdout
