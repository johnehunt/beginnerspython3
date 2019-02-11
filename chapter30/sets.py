basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed
print(len(basket))
basket.remove('apple')
basket.discard('apricot')
print(basket)

basket.add('apricot')
print(basket)

basket = {'apple', 'orange', 'banana'}
basket.update(['apricot', 'mango', 'grapefruit'])
print(basket)

basket.clear()
print(basket)

s1 = {'apple', 'orange', 'banana'}
s2 = {'grapefruit', 'lime', 'banana'}
print('Union:', s1 | s2)
print('Intersection:', s1 & s2)
print('Difference:', s1 - s2)
print('Symmetric Difference:', s1 ^ s2)