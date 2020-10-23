age = 19
if age >= 18:
	print("You are old enough to vote!")

if age < 4:
	price = 0
elif age < 18:
	price = 5
else:
	price = 10

print("your admission cost is $" + str(price) + ".")

requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding " * requested_topping + ".")
	print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?\n")
	
available_toppings = ['mushrooms','olives','green peppers', 'pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry, we don't have " + requested_topping + ".")
		
print("\nFinished making your pizza!")
