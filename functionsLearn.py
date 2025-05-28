a = 4

def myFunction(x, b):
    print("the king " + x)
    print(a+b)
    print(__file__)
    print(f"global variable is {a} and local variable is {b}")

myFunction('43', 20)