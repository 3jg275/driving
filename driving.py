country = input('Nation plz ')
age = input('plz input your age ')
age = int(age)
if country == 'Taiwan':
    if age >= 18:
        print('Able to get license')
    else:
        print('Not yet')