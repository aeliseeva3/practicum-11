lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
start = int(input())
end = int(input())

slice_to_move = lst1[start-1:end]  
slice_reversed = slice_to_move[::-1]

foe element in slice_reversed:
	lst2.append(element)

del lst1[start-1:end]

print(lst1)
print(lst2)

