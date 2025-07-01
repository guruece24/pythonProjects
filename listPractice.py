myList = ["guru", "prasad", "king", "indian", 423, 42.43, -42, 'f']
myList1 = ["p", "q"]


for value in myList:
    if(type(value) is int):
        print(f"{value} and its datatype is {type(value)} and its index is {myList.index(value)}")
    elif (type(value) is float):
        print(f"{value} and its datatype is {type(value)} and its index is {myList.index(value)}")
    else:
         print(f"{value} and its datatype is {type(value)} and its index is {myList.index(value)}")

myList.append("superstar")
print("\n")
print("after append\n", myList)

print("\n")
print("print top 3\n", myList[0:3])

print("\n")
print("print last 3\n", myList[-3:])

print("\n")
print("print middle 3\n", myList[2:8])

myList.insert(0,"whoamI")
print("\n")
print("after insert\n", myList)

myList.remove("f")
print("\n")
print("after remove\n", myList)

myList.pop()
print("\n")
print("after pop\n", myList)

myList.reverse()
print("\n")
print("after reverse\n", myList)

myList.append("indian")
print("\n")
print("after append\n", myList)
print("\nnumber of times present of INDIAN in the list is\n", myList.count("indian"))

print("\n")
if "king" in ["guru", "prasad", "king", "indian", 423, 42.43, -42, 'f']:
    print(["guru", "prasad", "king", "indian", 423, 42.43, -42, 'f'].index("king"))

myList[4] += "_replaced"
print("\n")
print("after replacing\n", myList)

for i, location in enumerate(myList):
    print(i, location)

