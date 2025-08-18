#impure function
#global variable - reference variable
total = 0

def addTotal(amount):
     global total
     total += amount
     print("total: " + str(total))

def test(name="guru"):
    print("total:" + str(total))
    print("named parameteres: " + name)


addTotal(10)
test()