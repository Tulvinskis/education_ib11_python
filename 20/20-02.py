k_list = []
klass = int(input())
for i in range(klass):
    k_values = []
    n = int(input())
    for j in range(n):
        last_name, estimation = input("Фамилия, оценка: ").split()
        k_values.append(int(estimation) == 5)
    k_list.append(any(k_values))
if all (k_list):
    print("ДА")
else:
    print("НЕТ")