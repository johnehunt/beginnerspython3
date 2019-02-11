print("It's the day")
print('She said "hello" to everyone')

string_1 = 'Good'
string_2 = " day"
string_3 = string_1 + string_2
print(string_3)
print(len(string_3))

z = """
Hello
  World
"""
print(z)

my_variable = 'John'
print(type(my_variable))

my_string = 'Hello World'
print(my_string[4])
print(my_string[1:5])
print(my_string[:5])
print(my_string[2:])

print(z.upper())

print(type(b'abc'))

title = 'The Good, The Bad, and the Ugly'
print(title.split(' '))
print(title.split(','))

print('*' * 10)
print('Hi' * 10)

some_string = 'Hello World'
print('Testing a String')
print('some_string', some_string)
print("some_string.startswith('H')", some_string.startswith('H'))
print("some_string.startswith('h')", some_string.startswith('h'))
print("some_string.endswith('d')", some_string.endswith('d'))
print('some_string.istitle()', some_string.istitle())
print('some_string.isupper()', some_string.isupper())
print('some_string.islower()', some_string.islower())
print('some_string.isalpha()', some_string.isalpha())

print('String conversions')
print('some_string.upper()', some_string.upper())
print('some_string.lower()', some_string.lower())
print('some_string.title()', some_string.title())
print('some_string.swapcase()', some_string.swapcase())
print('String leading, trailing spaces', "   xyz   ".strip())

my_string = 'Count, the number     of spaces'
print("my_string.count(' ')", my_string.count(' '))

welcome_message = 'Hello World!'
print(welcome_message.replace("Hello", "Goodbye"))


print(some_string.isupper)
print(some_string.isupper())