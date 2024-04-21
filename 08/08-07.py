n = int(input())
strings = []
for i in range(n):
    strings.append(input())
for i in range(n):
    if "кот" in strings[i]:
        index = strings[i].index("кот") + 1
        print(i+1, index)
