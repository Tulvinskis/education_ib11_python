num_lines = int(input())
found_cat = False

for _ in range(num_lines):
    line = input()
    if not found_cat and ("Кот" in line or "кот" in line):
        found_cat = True
    if "Пёс" in line or "пёс" in line:
        found_cat = False
    if found_cat:
        print("МЯУ")
    else:
        print("НЕТ")