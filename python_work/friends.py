names = ['victor', 'isaac', 'gabriel']

'''print(names[0].title()) 
print(names[1].title()) 
print(names[2].title())

print("Olá " + names[0].title() + "! Vamos criar um projeto em Python?")

print("Olá " + names[1].title() + "! Vamos criar um projeto em Python?")

print("Olá " + names[2].title() + "! Vamos criar um projeto em Python?")'''

for name in names:
	print(name.title())
	message = "\nOlá " + name.title() + "! Vamos criar um projeto em Python?\n"
	print(message)