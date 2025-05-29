# app.py
# This is a test commit to test the github actions workflows
#self-host runner test
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
