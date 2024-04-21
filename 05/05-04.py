n = int(input())
found_cat = False
for _ in range(n):
    line = input()
    if "Кот" in line or "кот" in line:
        found_cat = True
        break
if found_cat:
    print("МЯУ")
else:
    print("НЕТ")