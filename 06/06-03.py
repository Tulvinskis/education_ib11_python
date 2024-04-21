a = set()
b = set()
c = 0
english_students = int(input())
german_students = int(input())
for i in range(english_students):
    fam_1 = input()
    a.add(fam_1)
print()
for i in range(german_students):
    fam_2 = input()
    b.add(fam_2)
count = len(a ^ b)
if count > 0:
    print(count)
else:
    print("NO")