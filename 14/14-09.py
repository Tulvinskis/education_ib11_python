def ask_password():
    for i in range(0, 3):
        n = input()
        if n == "password":
            print("Пароль принят")
            break
        else:
            print("В доступе отказано")


ask_password()