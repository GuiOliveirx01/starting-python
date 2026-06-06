"""
Concepts practiced:
- Variables
- f-strings
- String methods
- String formatting
- Escape characters

Methods:
- .lower() -> Returns a copy of the string with all characters lowercase.
- .upper() -> Returns a copy of the string with all characters uppercase.
- .title() -> Returns a copy of the string with the first letter of each word capitalized.
- .lstrip() -> Removes leading whitespace.
- .rstrip() -> Removes trailing whitespace.
- .strip() -> Removes leading and trailing whitespace.

Escape characters:
- \t -> Inserts a horizontal tab.
- \n -> Inserts a new line.
"""

user_name = "Guilherme"

print(f"Alô {user_name}, você gostaria de aprender um pouco de Python hoje?")

person_name = "Ada Lovelace"

print(person_name.lower())
print(person_name.upper())
print(person_name.title())

print(
    'Albert Einstein certa vez disse: "A mente que se abre a uma nova ideia '
    'jamais voltará ao seu tamanho original."'
)

famous_person = "Robert Oppenheimer"

message = (
    f'"O otimista pensa que este é o melhor de todos os mundos possíveis. '
    f'O pessimista receia que isso seja verdade." – {famous_person}'
)

print(message)

# String containing extra whitespace characters.
another_name = "\tAlan Turing\n"

print(another_name)
print(another_name.lstrip())
print(another_name.rstrip())
print(another_name.strip())