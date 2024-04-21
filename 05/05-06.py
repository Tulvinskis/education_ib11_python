numbers_sum = 0
numbers_count = 0
while True:
    number = int(input())
    numbers_sum += number
    numbers_count += 1
    if numbers_sum == 10:
        break
print(numbers_count)