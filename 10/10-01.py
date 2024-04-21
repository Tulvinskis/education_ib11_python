number = []
a = 0
n = int(input())
for i in range(n):
    nums = int(input())
    number.append(nums)
chislo = int(input())
for i in range(n):
    for j in range(i + 1, n):
        if chislo == number[i] * number[j]:
            a = 1
if a == 1:
    print("ДА")
else:
    print("НЕТ")