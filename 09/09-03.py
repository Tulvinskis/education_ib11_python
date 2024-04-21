a = list()
for i in range(int(input())):
    a.append(input())
b = int(input())
for i in a:
    if b <= len(i):
        print(i[b - 1], end="")