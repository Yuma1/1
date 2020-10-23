import this

print("\nHello Python world")
message = "Hello Python world"
print(message)

message = "Hello Python Crash Course World"
print(message)


name = "harry potter"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "yuma"
last_name = "furuya"
full_name = first_name + " " + last_name

print(full_name)
print("Hello, " + full_name.title() + "!")
message = " Hello, " + full_name.title() + "! "
print(message.strip())

print("\tHello\nHello again.    f")

x = 4

#avoidng error
message = " Hello, " + str(23) + "! "

#-----List------
bicycles = ["trek", 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[-1])
print(bicycles[-2])

bicycles.append("yuma")
print(bicycles)

brand = []
brand.append("beams")
brand.append("mitsumine")
brand.append("takeokikuchi")
print(brand)

brand.insert(0,"unitedarrows")
print(brand)
brand.append("bananarepublic")
print(brand)

#------Organizing a List
print("\n-----organaizing a List-----")
brand.sort()
print(brand)
brand.sort(reverse=True)
print(brand)

print("Here is the original list:")
print(brand)
print("\nHere is the sorted list:")
print(sorted(brand))
print("\nHere is the original list again:")
print(brand)
brand.reverse()
print(brand)
print(len(brand))


print("\nThe countries that I have been to.")
countries = []
countries.append("Canada")
countries.append("America")
countries.append("Australia")
countries.append("Korea")
countries.append("China")

print(countries)
print(sorted(countries))
print(countries)
countries.reverse()
print(countries)
countries.reverse()
print(countries)
countries.sort()
print(countries)
countries.sort(reverse = True)
print(countries)
print(message)
print("\n")




