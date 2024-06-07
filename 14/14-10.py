def golden_ratio(i):
    n = [1, 1]
    for k in range(1000):
        n.append(n[k] + n[k + 1])
    print(n[i] / n[i - 1])


golden_ratio(4)