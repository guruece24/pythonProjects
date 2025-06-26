age = int(input('What is your age: '))
countryCode= 'IND'

if age >= 18:
    isLicense = input('Do you have license?: yes/no ')
    if isLicense.lower() != 'yes':
        print('Why cant you people take license instead of simply sitting')
        exit()
    isCountry = input('Are you Indian? yes/no ')
    if countryCode.lower() in ['ind', 'in','india'] and isCountry.lower() == 'yes':
        print('Great! I like people like you. You can drive')
        print(f'your country code is {countryCode}')
    ##elif isLicense.lower() == 'yes' and isCountry.lower() != 'yes':
    else:print('If you are an anti-indian, then what country license you possess. dont waste my time')
else:
    print('you are too young man. close the computer drink milk and sleep')