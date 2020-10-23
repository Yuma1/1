filename = "texts/learning_python.txt"

message = "I like YOU"

message.replace('like', 'love')

print(message.replace('like', 'love'))

with open(filename) as file_object:
	lines = file_object.readlines()

#lines.replace("can", "can't")
print(lines.replace('can', 'c'))
