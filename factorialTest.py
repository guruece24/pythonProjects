from datetime import datetime

def factorial(number):
    if not isinstance(number, int):
        raise TypeError("sorry. number must be an integer")
    if number < 0:
        raise ValueError("sorry. number must be positive or zero")
    def inner_factorial(number):
        print(number)
        if(number <= 1):
            return 1
        return number * inner_factorial(number-1)
    return inner_factorial(number)

print(factorial(5))


