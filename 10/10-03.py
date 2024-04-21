alphabet = []
n = int(input())
for i in range(n):
    alphabet.append(input())
for i in range(n):
    for j in range(i + 1, n):
        if alphabet[i] > alphabet[j]:
            alphabet[i], alphabet[j] = alphabet[j], alphabet[i]
for i in range(n):
    print(alphabet[i])