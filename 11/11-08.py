url = input()
key = input()
query = url.split('?')[1]
pairs = query.split('&')
for pair in pairs:
    k, v = pair.split('=')
    if k == key:
        print(v)
        break
