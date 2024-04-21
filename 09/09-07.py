words = list()
n = int(input())
for i in range(n):
    words.append(input())
a= int(input())
words_1 = list()
for i in range(a):
    words_1.append(input())
for i in words:
    search = True
    for j in words_1:
        if j not in i:
            search = False
    if search:
        print(i)