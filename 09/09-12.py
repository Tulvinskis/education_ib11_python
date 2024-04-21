num = input()
n = int(num[:4])
result = int(num[4:])
errors = list()
true_result = 0
for i in range(n):
    num = input()
    price = int(num[:7])
    summa = int(num[8:12])
    cost = int(num[13:])
    if price * summa != cost:
        errors.append(i+1)
    true_result += cost
print(result - true_result)
for a in errors:
    print(a, end=' ')