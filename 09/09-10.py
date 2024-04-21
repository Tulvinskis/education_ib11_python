numbers = list()
for i in range(int(input())):
    numbers.append(int(input()))
p = int(input())
q = int(input())
result = 0
for i in range(p-1, q):
    result += numbers[i]
print(result)