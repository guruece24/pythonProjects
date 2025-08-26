from functools import reduce


def even(num):
    if(num % 2== 0):
        return 'even'


a = [43,14, 92, 72, 35, 52, 64, 15, 90, 86]
b = filter(even, a)

c = filter(lambda num1: num1 % 2 != 0, a)

d = map(lambda num1: num1 % 2 != 0, a)

#e = reduce(lambda  num1: 'true' if num1 % 2 != 0 else 'false', a)
f=reduce(lambda x,y :x if x > y else y, a)

print(list(b))
print("using filter to check odd\n=======")
print(list(c))
print("using map to check odd\n=======")
print(list(d))
#print(e)
print(f)

