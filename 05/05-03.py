found_cat = False
line_number = 0

while True:
    line = input()
    line_number += 1

    if line == "СТОП":
        break

    if "Кот" in line or "кот" in line:
        found_cat = True
        break

if found_cat:
    print(line_number)
else:
    print(-1)
