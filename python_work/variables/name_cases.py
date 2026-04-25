# Mensagem pessoal
name = "Guilherme"
message = "Alô " + name + ", você gostaria de  aprender um pouco de Python hoje?"
print(message)

# Letras maiúsculas e minúsculas em nomes
name = "Ada Lovelace"
print(name.lower())
print(name.upper())  
print(name.title())

# Citações famosas
message = 'Albert Einstein certa vez disse: "A mente que se abre a uma nova ideia jamais voltará ao seu tamanho original".'
print(message)

famous_person = "Robert Oppenheimer"
message = '"O otimista pensa que este é o melhor de todos os mundos possíveis. O pessimista receia que isso seja verdade." – ' +famous_person
print(message)

# Removendo espaços em branco
name = "\tAlan Turing\n"
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip()) 