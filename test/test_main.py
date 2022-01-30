import main

def test_factorial():
    assert main.factorial(2) == 2
    assert main.factorial(4) == 24
    assert main.factorial(10) == 3628800
    assert main.factorial(1) == 1

def test_is_lower():
    assert main.is_lower("ala") == True
    assert main.is_lower("Kotek") == False
    assert main.is_lower("MlekO") == False
    assert main.is_lower("mleko") == True
