# Printing pout some strings containing quotes
print("It's the day")
print('She said "hello" to everyone')

# Concatenataing strings together
string_1 = 'Good'
string_2 = " day"
string_3 = string_1 + string_2
print(string_3)
print(len(string_3))

my_variable = 'Bob'
print(my_variable)
my_variable = "Eloise"
print(my_variable)

# A multi line string
z = """
Hello
  World
"""
print(z)

# Printing the type of a string - its class string
my_variable = 'Bob'
print(type(my_variable))

# Accessing parts of a string
my_string = 'Hello World'
print(my_string[4])
print(my_string[1:5])
print(my_string[:5])
print(my_string[2:])

# Converting a string to uppper case
print(z.upper())

print(type(b'abc'))

# Splitting a string up
title = 'The Good, The Bad, and the Ugly'
print('Source string:', title)
print('Split using a space')
print(title.split(' '))
print('Split using a comma')
print(title.split(','))

# Counting howmany times a substring appears in a string
my_string = 'Count, the number     of spaces'
print("my_string.count(' '):", my_string.count(' '))

# String replacement / substitution
welcome_message = 'Hello World!'
print(welcome_message.replace("Hello", "Goodbye"))

# Generating multiple strings
print('*' * 10)
print('Hi' * 10)

# Testing strings containing another string
print('Edward Alan Rawlings'.find('Alan'))
print('Edward John Rawlings'.find('Alan'))

print('James' == 'James') # prints True
print('James' == 'John') # prints False
print('James' != 'John') # prints True
print('James' == 'james') # prints False

# Various different string operations
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

# String conversions
print('String conversions')
print('-' * 20)
print('some_string.upper()', some_string.upper())
print('some_string.lower()', some_string.lower())
print('some_string.title()', some_string.title())
print('some_string.swapcase()', some_string.swapcase())
print('String leading, trailing spaces', "   xyz   ".strip())

# Adding a number to a string - need to use the str() function
msg = 'Hello Lloyd you are ' + str(21)
print(msg)
