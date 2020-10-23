user_0 = {
	'username': 'efermi',
	'first': 'enfico',
	'last': 'fermi',
	}
	
for key, value in user_0.items():
	print("\nKey: " + key)
	print("Value: " + value)
print("\n")

#-------------Loopoing through dictionary's keys in order-------

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

print(favorite_languages)

friends = ['phil','sarah']
for name in favorite_languages.keys():
	print(name.title())
	
	if name in friends:
		print(" Hi " + name.title() +
		", I see your favorite language is " +
		favorite_languages[name].title() + "!")
		
if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll.\n")

for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.\n")

print("the following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())

print("\n")
#-----------Set-----------
for language in set(favorite_languages.values()):
	print(language.title())




