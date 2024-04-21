shag = int(input())
text = input()
for i in text:
    print(chr(ord(i) + shag), end="")