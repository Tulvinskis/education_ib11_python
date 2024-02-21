password = input("Введите пароль: ")
confirm_password = input("Подтвердите пароль: ")

while True:
    if len(password) < 8:
        print("Короткий!")
    elif "123" in password:
        print("Простой!")
    elif password != confirm_password:
        print("Различаются.")
    else:
        print("OK")
    break