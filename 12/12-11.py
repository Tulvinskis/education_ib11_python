def build_pyramid(cube_sides):
    pyramid = []
    while cube_sides:
        if len(cube_sides) == 1:
            return "НЕТ"
        pyramid.append(cube_sides.pop(0))
        pyramid.append(cube_sides.pop())
        for i in range(len(pyramid) // 2):
            if pyramid[i] >= pyramid[-1]:
                return "НЕТ"
        pyramid.sort(reverse=True)
    return pyramid

def main():
    n = int(input("Введите количество раундов игры: "))
    for _ in range(n):
        sides = list(map(int, input().split()))
        result = build_pyramid(sides)
        print(" ".join(map(str, result)))
if __name__ == "__main__":
    main()
