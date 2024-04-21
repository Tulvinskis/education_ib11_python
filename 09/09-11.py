white_list = list()
for i in range(int(input())):
    white_list.append(input())
search = list()
for j in range(int(input())):
    search.append(input())
for a in search:
    if a in white_list:
        print(a)