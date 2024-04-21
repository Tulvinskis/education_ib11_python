s = input().lower()
print(max(s.count(char) for char in set(s)))