import random
stage_1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
stage_2 = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
stage_3 = ['2', '3', '4', '5', '6', '7', '8', '9']
stage_4 = stage_1 + stage_2 + stage_3

def generate_password(m):
    password = []
    password.append(random.choice(stage_1))
    password.append(random.choice(stage_2))
    password.append(random.choice(stage_3))
    for i in range (0, m - 3):
        password.append(random.choice(stage_4))
    random.shuffle(password)
    return ''.join(password)

def main(n, m):
    list_password = []
    while len(list_password) < n:
        list_password.append(generate_password(m))
    return list_password

print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")
