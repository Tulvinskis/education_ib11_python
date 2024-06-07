def who_are_you_and_hello():
    name = ""
    while not name or not name.isalpha() or not name[0].isupper() or not name[1:].islower():
        name = input("What is your name?")
    print(f"Привет, {name}")


who_are_you_and_hello()