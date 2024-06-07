def print_document(pages):
    for i in pages:
        if "Секретно" in i:
            print("Дальнейшие материалы засекречены")
            return
        print(i, end="\n")
    print("Напечатано без купюр")


print_document(["Пустой трёп", "который", "никому не интересен"])