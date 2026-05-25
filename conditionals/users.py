current_users = ['Guilherme', 'Maria', 'Gabriel', 'Ana', 'Marcelo']

new_users = ['Pedro', 'Lucas', 'Mateo', 'Marcelo', 'Ana']

for new_user in new_users:
    if new_user.title() in current_users:
        print("Este nome já está sendo usado, por favor selecione outro nome.")
    else:
        print("Este nome está disponível.")