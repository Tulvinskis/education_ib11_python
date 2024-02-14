login = input("Введите желаемый логин: ")
recovery_email = input("Введите резервный адрес электронной почты: ")

if "@" in login or "@" not in recovery_email:
    print("Ошибка! Введены некорректные данные.")
else:
    print("Регистрация прошла успешно!")