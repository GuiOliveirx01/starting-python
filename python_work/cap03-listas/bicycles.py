# Uma lista armazena um conjunto de informações.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Para acessar um item específico da lista, informe a sua posição dentro dela.
print(bicycles[0])
print(bicycles[0].title())

# As posições em uma lista começam em 0, então [1] e [3] referem-se ao 2º e 4º itens.
print(bicycles[1])
print(bicycles[3])

# A posição [-1] sempre acessa o último item da lista.
print(bicycles[-1])

# Podemos usar concatenação em itens individuais de uma lista.
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)