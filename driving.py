country = input('Nation plz ')
country = str(country)
age = input('plz input your age ')
age = int(age)
if country == 'Taiwan':
    if age >= 18:
        print('Able to get license')
    else:
        print('Not yet')
elif country == 'us':
    if age >= 16:
        print('Able to get license')
    else:
        print('Not yet')