for i in range(int(input())):
    s = input()
    if s.find("кот") != -1:
        print(i + 1, s.find("кот") + 1)