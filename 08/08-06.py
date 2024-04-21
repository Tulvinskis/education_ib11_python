mx = int(input())
n = int(input())

for i in range(n):
    text = input()
    if len(text) > mx:
        text = text[:mx - 3] + "..."
    print(text)