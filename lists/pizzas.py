pizzas = [
    'calabresa',
    'cheddar e bacon', 
    'frango com catupiry'
]

for pizza in pizzas:
    print(f"Gosto de pizza sabor {pizza}.")
    
print("Eu realmente adoro pizza!")

friends_pizzas = pizzas[:]

pizzas.append('portuguesa')
friends_pizzas.append('marguerita')

print("\nMinhas pizzas favoritas são:")

for pizza in pizzas:
    print(f"- {pizza}")

print("\nAs pizzas favoritas do meu amigo são:")

for pizza in friends_pizzas:
    print(f"- {pizza}")