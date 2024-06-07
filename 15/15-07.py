def find_mountain(heightsMap):
    a = 0
    for i in range(len(heightsMap)):
        for j in range(len(heightsMap)):
            if heightsMap[i][j] > a:
                str, s, a, = i, j, heightsMap[i][j]
    return (str, s)


a = [[1, 3, 1], [3, 2, 5], [2, 2, 2]]
print(find_mountain(a))