number = int(input())
divisors = []

for numbers in range(1, abs(number) + 1):
    if number % numbers == 0:
        divisors.append(numbers)

print(divisors)

