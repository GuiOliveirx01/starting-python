motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Para mudar o valor de um item usamos essa sintaxe: 
motorcycles[0] = 'ducati'
print(motorcycles)

# .append() e .insert() adicionam um item na lista.
motorcycles.append('honda')
print(motorcycles)

motorcycles.insert(0, 'kawasaki')
print(motorcycles)

# del e .pop() removem um item da lista de acordo com sua posição
del motorcycles[0]
print(motorcycles)

# No método .pop() podemos usar o item após sua remoção.
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

# .remove() remove um item de acordo com seu valor
print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is to expensive for me.")