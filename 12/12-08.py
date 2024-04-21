text = "".join(input().lower().split())
a = list()
c = 0
sim = 0
for i in text:
    a.append(i)
for j in a:
    if a.count(j) > c:
        c = a.count(j)
        sim = j
print(sim)