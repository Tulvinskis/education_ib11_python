num = list()
n = int(input())
for i in range(n):
    num.append(int(input()))
for i in range(n - 1):
    print(num[i] + num[i + 1])