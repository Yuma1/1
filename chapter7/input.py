message = input("Tell me something, and I will repeat it back to you: ")
print(message)
name = input("Please enter your name: ")
print("Hello, " + name + "!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("Hello, " + name + "!")

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
	print("\nYou are tall enough to ride!")
else:
	print("\nYou will be able to ride when you are a little older.")


