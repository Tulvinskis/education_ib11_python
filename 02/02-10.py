# Считываем два дробных числа
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

# Считываем операцию
operation = input("Введите операцию (+, -, * или /): ")

# Выполняем операцию
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        result = "888888"  # Деление на ноль
    else:
        result = num1 / num2
else:
    result = "888888"  # Неизвестная операция

# Выводим результат
print(result)