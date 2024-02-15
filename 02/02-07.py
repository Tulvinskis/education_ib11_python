str = float(input())

if str < 0.000001 or str == 0:
    print(1000000)
else:
    print(str ** -1)