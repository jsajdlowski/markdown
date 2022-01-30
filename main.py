def factorial(n):
    if n >= 1:
        fact = 1
        for num in range(2, n + 1):
            fact *= num
        return fact

def is_lower(str):
    flag = False
    if str == str.lower():
        flag = True
    else:
        flag = False
    return flag

print(is_lower(0))