boris = int(input("Рост Бори (см): "))
vova = int(input("Рост Вовы (см): "))
dima = int(input("Рост Димы (см): "))

# Сортируем рост по убыванию
if boris > vova:
    if boris > dima:
        if vova > dima:
            print("Порядок роста в шеренге:")
            print(boris, "см")
            print(vova, "см")
            print(dima, "см")
        else:
            print("Порядок роста в шеренге:")
            print(boris, "см")
            print(dima, "см")
            print(vova, "см")
    else:
        print("Порядок роста в шеренге:")
        print(dima, "см")
        print(boris, "см")
        print(vova, "см")
else:
    if vova > dima:
        if boris > dima:
            print("Порядок роста в шеренге:")
            print(vova, "см")
            print(boris, "см")
            print(dima, "см")
        else:
            print("Порядок роста в шеренге:")
            print(vova, "см")
            print(dima, "см")
            print(boris, "см")
    else:
        print("Порядок роста в шеренге:")
        print(dima, "см")
        print(vova, "см")
        print(boris, "см")