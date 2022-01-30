import main

def test_factorial():
    assert main.factorial(2) == 2
    assert main.factorial(4) == 24
    assert main.factorial(10) == 3628800
    assert main.factorial(1) == 1

def test_subtraction():
    assert main.subtraction(4,5) == -1
    assert main.subtraction(5,4) == 1
    assert main.subtraction(4.5,4) == 0
