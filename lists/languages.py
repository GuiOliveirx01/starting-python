# ===== CREATING LIST =====
languages = []

print(languages)

print()

# ===== ADDING ITEMS =====
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

# ===== REMOVING ITEMS =====
del languages[0]
languages.pop(1)
languages.remove('C#')

print(languages)

print()

# ===== ORGANIZING LIST =====
languages.sort(reverse=True)
print(languages)

print()

print(sorted(languages))

print()

languages.reverse()
print(languages)

print(f"\nMy list contains {len(languages)} items.")