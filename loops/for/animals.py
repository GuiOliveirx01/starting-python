animals = [
    'hipopótamo',
    'elefante',
    'rinoceronte',
    'búfalo',
    'gnu',
]

for animal in animals:
    print(f"O {animal} é um mamífero.")

print("Todos eles comem toneladas de plantas e frutas!")

print("\nOs três primeiros animais da lista são:")

for animal in animals[0:3]:
    print(f"- {animal}")

print("\nOs três animais do meio da lista são:")

for animal in animals[1:4]:
    print(f"- {animal}")

print("\nOs três últimos animais da lista são:")

for animal in animals[-3:]:
    print(f"- {animal}")                                                                        