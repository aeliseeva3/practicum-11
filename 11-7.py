numbers = list(map(int, input().split()))
sum_even = sum(number for number in numbers if number % 2 == 0)
sum_odd = sum(number for number in numbers if number % 2 != 0)

print(f"сумма четных {sum_even}")
print(f"сумма нечетных {sum_odd}")

