for i in range(int(input())):
    text = input()
    if text[:4] == "####":
        continue
    if text[:2] == "%%":
        print(text[2:])
    else:
        print(text)