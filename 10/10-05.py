n = int(input())
a = 0
name = []
for i in range(n):
    name.append(input())
num = int(input())
repeat = int(input())
for i in range(0, n):
    if a != 2:
        print(name[i])
        a += 1
    else:
        a = 0