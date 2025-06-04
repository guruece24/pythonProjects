x=10.00
y="10"
z=10

a=int(y)

print(type(x))
print(type(y))
print(type(z))

print(type(a))

b="20"
c=y+b
print(f"{y} + {b} is {c}")


k=20
d=k+z
print(f"{k} + {z} is {d}")

e=x+k
print(f"{x} + {k} is {e}")
print(f"type of {e} is {type(e)}")

print(f"{y} + {b} after int typecasting is {int(y)+int(b)}")
print(f"{y} + {b} after float typecasting is {float(y)+float(b)}")

i='1'
print(f"{y} + {i} after int typecasting is {int(y)+int(i)}")

j="A"
#print(f"{y} + {i} after int typecasting is {int(y)+int(j)}")

m=8
n=4
o=m/n
p=m%n
print(f"{m} / {n} is {o}")
print(f"{m} % {n} is {p}")
print(f"{z} ** {z} is {z**z}")

print(f"{m} / {3} is {m/3}")
print(f"{m} // {3} is {m//3}")

print(f"{m} == {n} is {m==n}")
print(f"{m} != {n} is {m!=n}")
print(f"{m} >= {n} is {m>=n}")


if m % n == 0:
    print("true")
else:
    print("false")


s=True
t=False
print(f"{s} and {t} is {s and t}")
print(f"{t} and {s} is {t and s}")
print(f"{s} and {True} is {s and True}\n")
print(f"{s} or {t} is {s or t}")
print(f"{t} or {s} is {s or t}")
print(f"{s} or {True} is {s or True}")

print(f"{s} not is {not s}")