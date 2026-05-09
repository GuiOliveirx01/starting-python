# ===== PRIMEIROS CONVITES =====
names = ['maria clara', 'victor', 'isaac']

for name in names:
    print(f"Olá {name.title()}! Você está convidado(a) para um jantar hoje às 21h!")

# ===== SUBSTITUINDO CONVIDADO =====
print(f"\n{names[2].title()} não irá comparecer.\n")

names[2] = 'gabriel'

for name in names:
    print(f"Olá {name.title()}! Você está convidado(a) para um jantar hoje às 21h!")

# ==== ACRESCENTANDO CONVIDADOS ====
print("\nGalera! Encontrei uma mesa de jantar que cabe mais pessoas!\n")

names.insert(0, 'ana beatriz')
names.insert(2, 'marcelo')
names.append('valeska')

print(f"Agora estou convidando {len(names)} pessoas para o jantar!\n")

for name in names:
    print(f"Olá {name.title()}! Você está convidado(a) para um jantar hoje às 21h!")

# ===== REDUZINDO CONVIDADOS =====
print("\nInfelizmente a mesa não ficou pronta e só consigo convidar duas pessoas.\n")

# Remove nomes até restarem apenas dois convidados
while len(names) > 2:
    removed = names.pop()
    print(f"Sinto muito por não poder te convidar {removed.title()}.")

print()

for name in names:
    print(f"{name.title()}, você ainda está convidado(a)!")

# Remove todos os nomes da lista
del names[:]
print(names)