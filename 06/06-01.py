first_list = set()
second_list = set()
while True:
    try:
        num = input()
        if num:
            first_list.add(num)
        else:
            break
    except EOFError:
        break
input()

while True:
    try:
        num = input()
        if num:
            second_list.add(num)
        else:
            break
    except EOFError:
        break

intersect = first_list.intersection(second_list)
if intersect:
    for num in intersect:
        print(num)
else:
    print("EMPTY")