text = input()
num = int(input())
if num > len(text) or num < 1:
    print("ОШИБКА")
else:
    print(text[num - 1])