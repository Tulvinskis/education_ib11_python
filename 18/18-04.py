def partial_sums(*n):
    res = [0]
    for i in range(len(n)):
        res.append(res[i] + n[i])
    return res

print(partial_sums(15))