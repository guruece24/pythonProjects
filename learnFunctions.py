def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

def concatenate(*args):
    total = 0
    for value in args:
        total+=value
    return total

def pairsPrint(**kwargs):
    for key,value in kwargs.items():
        print(f"key: {key} value:{value}")



# res = add(3,5)
# print(res)
#
# res = sub(3,5)
# print(res)
#
# res = multiply(3,5)
# print(res)
#
# res = divide(3,5)
# print(res)
