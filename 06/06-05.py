num_1 = set()
num_2 = set()
n = int(input())
n += int(input())
n += int(input())
for i in range(n):
    text = input()
    if not text in num_1:
        num_1.add(text)
    else:
        if not text in num_2:
            num_2.add(text)
        else:
            num_2.remove(text)
if num_2:
    print(len(num_2))
else:
    print("NO")