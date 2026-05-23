user_names = ['victor', 'maria', 'admin', 'pedro', 'isaac']

if user_names:
    for user_name in user_names:
        if user_name == 'admin':
            print(f"Olá {user_name.title()}, gostaria de ver um relatório de status?")
        else:
            print(f"Olá {user_name.title()}, obrigado por fazer login novamente.")
else:
    print("Precisamos encontrar usuários!")