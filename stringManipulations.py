my_name= "guruprasad is the legend.\nif you dont know, then, what else can be done.\n"

print(my_name.upper())
print(my_name.capitalize())
print(my_name.title())

mobile = "9686038349"
masked = mobile[:2] + "******" + mobile[-2:]
print(len(mobile))
print(len(masked))
print(mobile)
print(masked)

masked_replaced = masked.replace('*', '^')
print(masked_replaced)

print(my_name.split(' ', 2))
print(len( my_name.split(' ', 2)))
print(my_name.split(' ',2)[2])

print("two split explaining here")
print(my_name.split('.')[1].split(',')[2].strip())

if "legend" in my_name:
    print("\ngreat")

print("position is: ", my_name.find("legend"))

initials = [word[0].upper() for word in my_name.split()]
print(initials)
initials_joined = "".join(initials)
print(initials_joined)