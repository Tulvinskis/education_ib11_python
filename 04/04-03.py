kub = 0
n = int(input('Введите число: '))
for a in range(n + 1):
    print("Куб числа ", str(a), " равен",  str(kub ** 3 ))
    kub += 1