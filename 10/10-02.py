students = []
n = int(input())
for i in range(n):
    students.append(input())
for student in students:
    print(student)
print()
for student in students:
    if student[-1] in ['4', '5']:
        print(student)