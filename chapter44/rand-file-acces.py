f = open('text.txt', 'w')
f.write('abcdefghijklmnopqrstuvwxyz\n')

f.seek(10,0)
f.write('HELLO')
f.seek(6, 0)
f.write ('BOO')
f.close()

with open('text.txt', 'r') as f:
    for line in f:
        print(line, end='')
