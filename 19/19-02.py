def simple_map(transformation, values):
    res = []
    for element in values:
        res.append(transformation(element))
    return res


values = [1, 3, 1, 5, 7]
print(*simple_map(lambda x: x + 5, values))