n = int(input("Введите количество чисел: "))
result = int(input())
sign = 1

for i in range(1, n):
    num = int(input())
    if sign == 1:
        result += num
    else:
        result -= num
    sign *= -1

print(f"Знакочередующаяся сумма ряда: {result}")