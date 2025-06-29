names = ['saravanan', 'gowtham', 'guru', 'prasad', 'king', 'indian']
i=1

for test in names:
    print(f"the {i}th name in list is {test}")
    i=i+1

#while loop
pin = '1234'
entered_pin = ''
i=0

while(pin != entered_pin):
    if(i==3):
        print('access denied. thats it. your life is over')
        break
    else:
        entered_pin = input('enter the correct pin. only 3 attempts')
        i=i+1
        if (pin == entered_pin):
            print('access granted')
            break


print('\n')
n=[-10, 3,5,34,-53,-4,53]

for value in n:
    pass #future logic implementation
    if(value < 0):
        continue
    if(value > 0):
        print(value)

