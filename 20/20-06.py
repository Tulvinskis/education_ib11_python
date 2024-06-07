import sys

num = list(map(str.strip, sys.stdin))
num = [s.strip() for s in num]
comments = list(filter(lambda word: word[0] == '#', num))
for e in comments:
    print(f'Line {num.index(e) + 1}: {e[1:].strip()}')