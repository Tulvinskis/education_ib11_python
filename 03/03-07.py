number1, number2 = 1, 100
while True:
    x = (number1 + number2) // 2
    print("Твое число больше, меньше или равно", x, "?")
    t = int(input("1 - Больше, 2 - Меньше, 3 - Равно: "))
    if t == 3:
        print("Я угадал. Спасибо за игру.")
        break
    elif t == 1:
        number1 = x
    else:
        number2 = x
