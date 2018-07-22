miss = input('Babe, are you tired? ')

if miss == 'No':
    print('Everything is gotta be alright')
    print('Lean on me')
if miss == 'Yes':
	print('How badly you want it')
	print('What cannot kill you makes you stronger')
# 其實我覺得 One OK Rock 有點屁孩

mood = input('How was your boss today? (please scale from 1 to 10) ')
if int(mood) >= 6:
	print('Buy him a drink')
	print('         ...and fuck him')
if int(mood) <= 5:
	print('Just fuck him')

age = input('How old are you? ')
age = int(age)
her_age = age + 30
his_age = age - 12
if age >= 32:
	print('Your mom is ', her_age, 'years old')
if age <= 31:
	print('I am ', his_age, 'years old')