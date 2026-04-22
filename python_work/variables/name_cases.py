# Armazena o nome do usuário e cria uma mensagem de saudação personalizada
name = "Guilherme"
message = "Olá " + name + "! Vamos escrever um pouco de código Python hoje?"
print(message)

# Demonstra diferentes formas de formatação de texto (minúsculas, maiúsculas e título)
name = "Maria clara"
print(name.lower())   # Converte para letras minúsculas
print(name.upper())   # Converte para letras maiúsculas
print(name.title())   # Coloca a primeira letra de cada palavra em maiúscula

# Exibe uma citação famosa diretamente no código
print('Albert Einstein certa vez disse: "A mente que se abre a uma nova ideia jamais voltará ao seu tamanho original."')

# Armazena o nome de uma pessoa famosa e monta uma citação com concatenação
famous_person = "Robert Oppenheimer"
message = '"Agora eu me tornei a Morte, a destruidora de mundos." – ' + famous_person
print(message)

# Demonstra o uso de caracteres de espaço (\t e \n) e remoção de espaços extras
name = "\t Alan Turing \n"
print(name)   # Exibe o texto com espaços e quebras de linha
print(name.lstrip())  # Remove espaços à esquerda
print(name.rstrip())  # Remove espaços à direita
print(name.strip())   # Remove espaços dos dois lados