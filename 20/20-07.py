words = []
while True:
    word = input()
    if word == '':
        break
    words.append(word)

print(*sorted(words, key=lambda x: sum([ord(i) - ord('A') + 1 for i in x.upper()])), sep='\n')