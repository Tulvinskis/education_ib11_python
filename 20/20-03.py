sum_height = 0
count_students = 0

height = input()

while height != '':
    sum_height += int(height)
    count_students += 1
    height = input()

if count_students == 0:
    print(-1)
else:
    print(sum_height / count_students)