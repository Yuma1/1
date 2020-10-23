for value in range(1,5):
	print(value)
numbers = list(range(1,7))
print(numbers)

squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
	
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

nums = [value**2 for value in range(1,11)]
print(nums)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
print(players[0:3])
print(players[1:3])
print(players[:3])
print(players[2:])
print(players[-3:])

print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are :")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are :")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

for food in my_foods:
	print(food)

#-----Tuple-------
dimensions = (200,40)
for a in dimensions:
	print(a)
