n = int(input())
s_1 = set()
s_2 = set()
for i in range(n):
    fam = input()
    if fam in s_1:
        s_2.add(fam)
    else:
        s_1.add(fam)
itog = s_1 - s_2
itog = n - len(itog)
print(itog)