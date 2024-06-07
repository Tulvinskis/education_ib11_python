import sys
n = sys.stdin.read()
print(list(map(lambda x: x.lstrip().startswith("#"), n.split("\n"))).count(True))
