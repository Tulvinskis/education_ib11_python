stroka = []
for i in range(int(input())):
    stroka.append(input())
correct = sorted(stroka, key=len)
for a in correct:
    print(a)