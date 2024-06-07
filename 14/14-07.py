def print_statistics(arr):
    print(len(arr))
    if len(arr) == 0:
        print(0)
        print(0)
        print(0)
        print(0)

    else:
        print(sum(arr) / len (arr))
        print(min(arr))
        print(max(arr))
        arr.sort()
        if len(arr) % 2 == 0:
            a = len(arr) // 2
            b = a - 1
            print((arr[a]) + (arr[b]) / 2)
        else:
            print(arr[(len(arr) // 2)])

print_statistics([])