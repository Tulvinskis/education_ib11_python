words = []
for i in range(int(input())):
    words.append(input())
search = input()
for word in words:
    if search in word:
        print(word)