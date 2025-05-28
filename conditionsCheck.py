num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
num3 = input('Enter third number: ')

if(num1 > num2):
    if(num1 > num3):
        print("{0} is greater than {1}".format(num1, num3))
        print("inside nested if")
        print("inside nested once again")
    else:
        print("{0} is greater than {1}".format(num3, num1))
        print("inside nested else")
        print("inside nested else once again")
    print("outside nested")
    print("{0} is greater than {1}".format(num1, num2))
    print("inside if")
else:
    print("{0} is greater than {1}".format(num2, num1))
    print("inside else")