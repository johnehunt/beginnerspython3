a_global_count = 10

def some_func():
    a_local_variable = 100
    print('a_local_variable:', a_local_variable)
    print('a_global_count:', a_global_count)


some_func()

def my_function():
    a_variable = 100
    print('inside function:', a_variable)


a_variable = 25
my_function()
print('outside function:', a_variable)

max = 100
print('initial value of max:', max)
def print_max():
    global max
    max = max + 1
    print('inside function:', max)


print_max()
print('outside function:', max)


def outer():
    title = "original title"

    print('initial title:', title)

    def inner():
        nonlocal title
        title = "another title"
        print("inner:", title)

    inner()
    print("outer:", title)


outer()
