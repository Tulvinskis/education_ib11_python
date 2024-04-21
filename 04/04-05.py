nums = []
for i in range(6):
    num = int(input())
    if num != 0:
        nums.append(num)

result = 1
for num in nums:
    result *= num

print(result)