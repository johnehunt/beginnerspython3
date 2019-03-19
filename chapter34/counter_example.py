import collections

fruit = collections.Counter(['apple', 'orange', 'pear', 'apple', 'orange', 'apple'])
print(fruit)
print(fruit['orange'])

print('fruit.most_common(1):', fruit.most_common(1))

fruit1 = collections.Counter(['apple', 'orange', 'pear', 'orange'])
fruit2 = collections.Counter(['banana', 'apple', 'apple'])

print('fruit1:', fruit1)
print('fruit2:', fruit2)

print('fruit1 + fruit2:', fruit1 + fruit2)
print('fruit1 - fruit2:', fruit1 - fruit2)
# Union (max(fruit1[n], fruit2[n])
print('fruit1 | fruit2:', fruit1 | fruit2)
# Intersection (min(fruit1[n], fruit2[n])
print('fruit1 & fruit2:', fruit1 & fruit2)