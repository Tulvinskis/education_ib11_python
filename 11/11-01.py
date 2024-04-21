text = input().split()
answer = []
for i in range(2, len(text), 3):
    answer.append(text[i])
print(" ".join(answer))