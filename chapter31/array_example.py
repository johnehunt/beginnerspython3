""" Example of using Python array objkects - which are space efficient and fast
for iterative type processing. """

import array as arr

# Create an array Object
a = arr.array("I", [3, 6, 9])
print(a)
print('len(a):', len(a))
print(type(a))

# Append an element to the end of the array
a.append(4)
print(a)

print("First element:", a[0])
a[0] = 7
print("First element:", a[0])

# Remove element from an array
del a[0]
print(a)

# Loop through contents of array
for i in a:
    print(i)
