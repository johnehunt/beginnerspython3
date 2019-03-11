import fileinput

# Read multiple files
with fileinput.input(files=('textfile1.txt', 'textfile2.txt')) as f:
    for line in f:
        print(line, end='')
    print()

# Indicate some facilities
with fileinput.input(files=('textfile1.txt', 'textfile2.txt')) as f:
        line = f.readline()
        print('f.filename():', f.filename())
        print('f.isfirstline():', f.isfirstline())
        print('f.lineno():', f.lineno())
        print('f.filelineno():', f.filelineno())
        for line in f:
            print(line, end='')
