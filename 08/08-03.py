name = input()
alphabet = "abcdefghijklmnopqrstuvwxyz123456789_"
for char in name:
    if char not in alphabet:
        print("Неверный символ: " + char)
        break
else:
    print("OK")