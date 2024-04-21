word = input()
long = ""
short = ""
while word != "стоп":
    if len(word) > len(long):
        long = word
    if len(word) < len(long) or not short:
        short = word
    word = input()
fynded = True
for char in short:
    if char not in long:
        fynded = False
        break
if fynded:
    print("ДА")
else:
    print("НЕТ")