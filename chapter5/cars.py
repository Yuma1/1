cars = ['audi','bmw','subaru','toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())


print("\n")

age1 = 34
age2 = 25

if age1 > 30 or age2 > 30:
	print("true")
else:
	print("false")
	
if age1 > 30 and age2 > 30:
	print("true")
else:
	print("false")		


if 'mike' in cars:
	print("I have a mike")
else:
	print("I don't have a mike")
