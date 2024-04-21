book_home = set()
book_home_1 = int(input())
book_school = set()
book_school_1 = int(input())
for i in range(book_home_1):
    books = input()
    book_home.add(books)
for i in range(book_school_1):
    books = input()
    book_school.add(books)
    if books in book_home:
        print("YES")
    else:
        print("NO")