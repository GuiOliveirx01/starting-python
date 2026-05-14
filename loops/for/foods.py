my_foods = [
	'pizza', 
	'strogonnoff',
	'chocolate'
]

friend_foods = my_foods[:]

my_foods.append('batata frita')
friend_foods.append('sorvete')

print("Minhas comidas favoritas são:")

for food in my_foods:
	print(f"- {food}")

print("\nAs comidas favoritas do meu amigo são:")

for food in friend_foods:
	print(f"- {food}")