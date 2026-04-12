numbers = list(map(int, input().split()))

command = input()

direction = command[0]  
k = int(command[1:])

if direction == 'R':
    result = numbers[-k:] + numbers[:-k]
elif direction == 'L':
    result = numbers[k:] + numbers[:k]
else:
    print("Неверная команда")
    result = numbers

print(result)

