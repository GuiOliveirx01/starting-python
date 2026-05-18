# ===== PRIMEIROS CONVITES =====
guests = [
    'maria clara',
    'victor',
    'isaac'
]

for guest in guests:
    print(f"Olá {guest.title()}! Você está convidado(a) para um jantar hoje às 21h!")

# ===== SUBSTITUINDO CONVIDADO =====
print(f"\n{guests[2].title()} não irá comparecer.\n")

guests[2] = 'gabriel'

for guest in guests:
    print(f"Olá {guest.title()}! Você está convidado(a) para um jantar hoje às 21h!")

# ===== ACRESCENTANDO CONVIDADOS =====
print("\nGalera! Encontrei uma mesa de jantar que cabe mais pessoas!\n")

guests.insert(0, 'ana beatriz')
guests.insert(2, 'marcelo')
guests.append('valeska')

print(f"Agora estou convidando {len(guests)} pessoas para o jantar!\n")

for guest in guests:
    print(f"Olá {guest.title()}! Você está convidado(a) para um jantar hoje às 21h!")

# ===== REDUZINDO CONVIDADOS =====
print("\nInfelizmente a mesa não ficou pronta e só consigo convidar duas pessoas.\n")

# Remove nomes até restarem apenas dois convidados
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sinto muito por não poder te convidar {removed_guest.title()}.")

print()

for guest in guests:
    print(f"{guest.title()}, você ainda está convidado(a)!")

# Remove todos os nomes da lista
del guests[:]

print(guests)