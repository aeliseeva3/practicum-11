numbers = []
for _ in range(10):
    num = int(input())
    numbers.append(num)

new_list = []
for index in range(1, 9):  
    sum_neighbors = numbers[index - 1] + numbers[index + 1]
    new_list.append(sum_neighbors)

print(new_list)

