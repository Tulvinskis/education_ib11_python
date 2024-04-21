text = input()
print(*[i for i in input().split() if text.upper() in i.upper()], sep='\n')