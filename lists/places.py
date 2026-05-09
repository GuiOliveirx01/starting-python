places = ['nova zelândia', 'canadá', 'japão', 'estados unidos', 'austrália']

print("Here is the orginal list:")
print(places)

# sorted() cria uma versão ordenada sem alterar a lista original
print("\nHere is the sorted list:")
print(sorted(places))

print("\nHere is the original list again:")
print(places)

# reverse() inverte a ordem atual da lista
places.reverse()
print("\nHere is the reverse list:")
print(places)

places.reverse()
print("\nHere is the original list one more time:")
print(places)

# sort() altera permanentemente a lista
places.sort()
print("\nHere is the sorted list again:")
print(places)

# Ordena em ordem reversa (Z → A)
places.sort(reverse=True)
print("\nHere is the reverse sorted list:")
print(places)