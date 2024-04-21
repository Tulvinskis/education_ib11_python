n = input()
while n[0] != '1' and int(n) < 1000000000:
    n = str(int(n) * int(n[0]))
print(n)