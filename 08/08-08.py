moneta = input()
a = 0
b = 0
mx = 0
for i in moneta:
    if i == "о" and b == 0:
        a += 1
    elif i == "о" and b != 0:
        a = 1
        b = 0
    else:
        b = 1
    if a > mx:
        mx = a
print(mx)