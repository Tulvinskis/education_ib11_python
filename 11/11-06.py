recept = []
for i in range(int(input())):
    punkt = input()
    if 'лук' in punkt:
        continue
    recept.append(punkt)
print(", ".join(recept))