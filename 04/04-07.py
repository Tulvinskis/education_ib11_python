number = int(input())
divisors = ""

for i in range(1, number + 1):
    if number % i == 0:
        divisors += str(i) + " "

if divisors == "1 " + str(number) + " ":
    is_prime = "ПРОСТОЕ"
else:
    is_prime = "НЕТ"

print(divisors.strip())
print(is_prime)