money_1 = list()
money_2 = list()
n = int(input())
for i in range(n):
    money_1.append(int(input()))
for i in money_1:
    print(i)
print()
for i in range(n):
    money_2.append(money_1[i] * 3)
for i in money_2:
    print(i)