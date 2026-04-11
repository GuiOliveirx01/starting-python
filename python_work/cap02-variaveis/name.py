# Tudo o que estiver entre aspas é considerado uma string
name = "ada lovelace"

# A função .title() deixa a primeira letra de cada palavra maiúscula
print(name.title())

name = "Ada Lovelace"
# .upper() converte todas as letras para maiúsculas
print(name.upper())

# .lower() converte todas as letras para minúsculas.
print(name.lower())

# O símbolo '+' pode combinar variáveis ​​e strings.
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
message = "Hello, " + full_name.title() + "!"
print(message)

print("Python")
# '\t' cria um espaço em branco.
print("\tPython")
# '\n' cria uma quebra de linha.
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")