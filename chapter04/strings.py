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

my_variable = 'Bob'
print(type(my_variable))

my_string = 'Hello World'
print(my_string[4])
print(my_string[1:5])
print(my_string[:5])
print(my_string[2:])

print(z.upper())

print(type(b'abc'))

title = 'The Good, The Bad, and the Ugly'
print('Source string:', title)
print('Split using a space')
print(title.split(' '))
print('Split using a comma')
print(title.split(','))

my_string = 'Count, the number     of spaces'
print("my_string.count(' '):", my_string.count(' '))

welcome_message = 'Hello World!'
print(welcome_message.replace("Hello", "Goodbye"))

print('*' * 10)
print('Hi' * 10)

print('Edward Alan Rawlings'.find('Alan'))
print('Edward John Rawlings'.find('Alan'))

print('James' == 'James') # prints True
print('James' == 'John') # prints False
print('James' != 'John') # prints True
print('James' == 'james') # prints False

some_string = 'Hello World'
print('Testing a String')
print('-' * 20)
print('some_string', some_string)
print("some_string.startswith('H')", some_string.startswith('H'))
print("some_string.startswith('h')", some_string.startswith('h'))
print("some_string.endswith('d')", some_string.endswith('d'))
print('some_string.istitle()', some_string.istitle())
print('some_string.isupper()', some_string.isupper())
print('some_string.islower()', some_string.islower())
print('some_string.isalpha()', some_string.isalpha())

print('String conversions')
print('-' * 20)
print('some_string.upper()', some_string.upper())
print('some_string.lower()', some_string.lower())
print('some_string.title()', some_string.title())
print('some_string.swapcase()', some_string.swapcase())
print('String leading, trailing spaces', "   xyz   ".strip())

print(some_string.isupper)
print(some_string.isupper())

msg = 'Hello Lloyd you are ' + str(21)
print(msg)
