n = set()
for i in range(int(input())):
    n.add(input())
for i in range(int(input())):
    ingred = input()
    recept = set()
    for j in range(int(input())):
        recept.add(input())
    if len(recept & n) == len(recept):
        print(ingred)