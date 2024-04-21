english_lang = int(input())
german_lang = int(input())
a = set()
b = set()
for i in range(english_lang + german_lang):
    surname = input()
    if surname in a:
        b.add(surname)
    else:
        a.add(surname)
minus = a - b
if not minus:
    print('NO')
else:
    print(len(minus))