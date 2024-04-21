a = []
for i in range(int(input()[1:])):
    s = input()
    if "#" in s.split():
        n = s.index("#")
        s = "".join(s[:n])
    a.append(s)
for i in range(len(a)):
    print(a[i])