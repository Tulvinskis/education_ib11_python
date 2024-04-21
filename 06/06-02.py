cities = set()
n = int(input())
for _ in range(n):
    city = input()
    if city in cities:
        print("TRY ANOTHER")
    else:
        cities.add(city)
        print("OK")