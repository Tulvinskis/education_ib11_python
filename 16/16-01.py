PI = 3.14159


def circle_length(radius):
    return 2 * PI * radius


def circle_area(radius):
    return PI * radius * radius


radius = float(input())

length = circle_length(radius)


print(length)