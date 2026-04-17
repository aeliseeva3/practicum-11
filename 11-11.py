numbers = list(map(int, input().split()))

command = input()

direction = command[0]  
number = int(command[1:])

if direction == 'R':
    result = numbers[-number:] + numbers[:-number]
elif direction == 'L':
    result = numbers[number:] + numbers[:number]
else:
    print("Неверная команда")
    result = numbers

print(result)

