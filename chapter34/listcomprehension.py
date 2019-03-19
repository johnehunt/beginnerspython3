# List Comprehension examples


list1 = [1, 2, 3, 4, 5, 6]
print('list1:', list1)

list2 = [item + 1 for item in list1]
print('list2:', list2)

list3 = [item + 1 for item in list1 if item % 2 == 0]
print('list3:', list3)
