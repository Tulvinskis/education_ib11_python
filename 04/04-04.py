n = int(input("Введите целое неотрицательное число: "))
factorial = 1
if n < 0:
    print("Факториал отрицательного числа не дан")
elif n == 0:
    print("Равен 1")
else:
    for i in range(1, n + 1):
        factorial *= i
print(f"Факториал числа {n} равен {factorial}")
