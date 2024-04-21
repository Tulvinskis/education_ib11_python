for i in range(int(input())):
    text = input()
    if "Не " == text[:3] or "не " == text[:3]:
        print(text[3::])
    else:
        print(text)