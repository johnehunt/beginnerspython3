def grep(pattern):
    print('Looking for', pattern)
    try:
        while True:
            line = yield
            if pattern in line:
                print(line)
    except GeneratorExit:
        print('Exiting the Co-routine')


print('Starting')
# Initialise the coroutine
g = grep('Python')

# prime the coroutine
next(g)

# Send data to the coroutine
g.send('Java is cool')
g.send('C++ is cool')
g.send('Python is cool')

# now close the coroutine
g.close()
print('Done')
