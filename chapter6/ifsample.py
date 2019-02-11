# this is the first comment
num = int(input('Enter a number: '))
if num < 0:
    print(num, ' is negative')

print('-' * 25)

num = int(input('Enter another number: '))
if num > 0:
    print(num, ' is positive')
    print(num, ' squared is ', num * num)

print('Bye')

print('-' * 25)

num = int(input('Enter yet another number: '))
if num < 0:
    print('Its negative')
else:
    print('Its not negative')

print('-' * 25)

savings = float(input("Enter how much you have in savings: "))
if savings == 0:
    print("Sorry no savings")
elif savings < 500:
    print('Well done')
elif savings < 1000:
    print('Thats a tidy sum')
elif savings < 10000:
    print('Welcome Sir!')
else:
    print('Thank you')

print('-' * 25)

num = int(input('Enter a simple number: '))
result = (-1 if num < 0 else 1)
print('Result is ', result)

snowing = True
temp = -1
if temp < 0:
    print('It is freezing')
    if snowing:
        print('Put on boots')
    print('Time for Hot Chocloate')
print('Bye')

print('-' * 25)
age = 15
status = ''
if (age > 12) and age < 20:
    status = 'teenager'
else:
    status = 'not teenager'
print(status)

status = ('teenager' if age > 12 and age < 20 else 'not teenager')
print(status)
