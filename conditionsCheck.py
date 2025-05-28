num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))

if num1 > num2:
    if num1 >= num3:
        print("\t{0} is greater than {1}".format(num1, num3))
        print("\tinside nested if")
        print("\tinside nested once again")
    else:
        print("\t{0} is greater than {1}".format(num3, num1))
        print("\tinside nested else")
        print("\tinside nested else once again")
    print("outside nested")
    print("{0} is greater than {1}".format(num1, num2))
    print("inside main if")
else:
    print("{0} is greater than {1}".format(num2, num1))
    print("inside else")