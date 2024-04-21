n = int(input())
fam = set()
for i in range(n):
    num_fam = int(input())
    for j in range(num_fam):
        fam_work = input()
        fam.add(fam_work)

fam_all = set()
for fam_work in fam:
    if len(fam) == n:
        fam_all.add(fam_work)

if fam_all:
    for fam_work in fam_all:
        print(fam_work)