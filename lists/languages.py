# ======= CRIANDO LISTA =======
languages = []
print(languages)

print()

# ======= ADICIONANDO ITENS =======
languages.append('Python')
languages.append('JavaScript')
languages.append('C#')

print(languages)

print()

languages.insert(1, 'Java')
languages.insert(3, 'TypeScript')
languages.insert(5, 'Go')

print(languages)

print()

# ======= REMOVENDO ITENS =======
del languages[0]
languages.pop(1)
languages.remove('C#')

print(languages)

print()

# ======= ORGANIZANDO LISTA =======
languages.sort(reverse=True)
print(languages)

print()

print(sorted(languages))

print()

languages.reverse
print(languages)

print(f"\nMy list contains {len(languages)} items.")