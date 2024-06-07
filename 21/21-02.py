import random
n = int(input("Введите кол-во учеников: "))
students = [input() for i in range(n)]
secret_friends = students.copy()
random.shuffle(secret_friends)

while any(students[i] == secret_friends[i] for i in range(n)):
    random.shuffle(secret_friends)

for i in range(n):
    print(f"{students[i]} - {secret_friends[i]}")