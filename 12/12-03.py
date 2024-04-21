numbers = [int(a) for a in input().split()]
x, y = [int(b) for b in input().split()]
print(sum(numbers[x:y + 1]))