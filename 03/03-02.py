password = input("Введите пароль: ")

while len(password) < 8:
    print("Короткий!")
    break

confirm_password = input("Подтвердите пароль: ")

if password != confirm_password:
    print("Различаются.")
else:
    print("OK")