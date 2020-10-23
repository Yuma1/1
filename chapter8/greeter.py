def greet_user():
	"""Display a simple greeting."""
	print("Hello!")

def greet_user2(username):
	"""Display a simple greeting."""
	print("Hello, " + username)

def get_formatted_name(first_name, last_name, middle_name=''):
	"""Return a fullname, neatly formatted."""
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()
	
def print_models(unprinted_designs, completed_models):
	"""Simulate printing each design, until none are left.
	Move each design to completed_models after printing."""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		
		#Simulate creating a 3D print from the design.
		print("Printing model: " + current_design)
		completed_models.append(current_design)
		
def show_completed_models(completed_models):
	"""Show all the models that were pritned."""
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

def build_profile(first, last, **user_info): # '**' means a dictionary
	"""Build a dictionary containing everything we know about a user."""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
		return profile

user_profile = build_profile('Yuma', 'Furuya', location = 'Japan', field = 'Computer Science')
print(user_profile)

greet_user()
greet_user2('LeBron')

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

#This is an infinite loop
while True:
	print("\nPlease tell me your name: ")
	f_name = input("First name: ")
	if f_name == 'q':
		break
	l_name = input("Last name: ")
	if l_name == 'q':
		break;
	formatted_name = get_formatted_name(f_name, l_name)
	print("\nHello, " + formatted_name + "!")

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)

#-----------------------------------



