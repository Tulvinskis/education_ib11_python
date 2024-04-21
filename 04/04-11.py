n = int(input())
total_iq = 0
count = 0
for _ in range(n):
    iq = int(input())

    if count == 0:
        print("0")
    else:
        average_iq = total_iq / count

        if iq > average_iq:
            print(">")
        elif iq < average_iq:
            print("<")
        else:
            print("0")

    total_iq += iq
    count += 1
