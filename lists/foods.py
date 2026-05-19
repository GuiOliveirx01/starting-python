my_foods = [
    'pizza',
    'strogonoff',
    'chocolate'
]

# Creates a copy of the list instead of sharing the same reference
friend_foods = my_foods[:]

my_foods.append('batata frita')
friend_foods.append('sorvete')

print("Minhas comidas favoritas são:")

for food in my_foods:
    print(f"- {food}")

print("\nAs comidas favoritas do meu amigo são:")

for food in friend_foods:
    print(f"- {food}")