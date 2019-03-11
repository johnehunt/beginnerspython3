"""This is a test module"""

print('Hello I am module 1')


def f1():
    print('f1[1]')


def f2():
    print('f2[1]')

def main():
    x = 1 + 2
    print('x is', x)
    f1()
    f2()

if __name__ == '__main__':
    main()

