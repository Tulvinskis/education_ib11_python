phone_book = {}
N = int(input())
for _ in range(N):
    phone, name = input().split()
    if name in phone_book:
        phone_book[name].append(phone)
    else:
        phone_book[name] = [phone]

M = int(input())
queries = []
for _ in range(M):
    queries.append(input())

for query in queries:
    if query in phone_book:
        print(' '.join(phone_book[query]))
    else:
        print('Нет в телефонной книге')
