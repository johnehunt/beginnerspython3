print('Writing file')
f = open('python1', 'w')
f.write('Hello from Python!!\n')
f.write('Working with files is easy...\n')
f.write('It is cool ...\n')
f.close()

print('Reading file')
f = open('python1', 'r')
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
print('---')
print(line1, end='')
print(line2, end='')
print(line3, end='')

f = open('python1', 'r')
i = 0
for line in f:
    print(i, ':', line, end='')
    i = i + 1
f.close()

f = open('python1', 'r')
l = [line.upper() for line in f]
f.close()
print(l)

f = open('python1', 'r')
try:
    for line in f:
        print(line, end='')
finally:
    f.close()

with open('python1', 'r') as f:
    for line in f:
        print(line, end='')

print('RAM')
f = open('python2', 'w')
f.write('abcdefghijklmnopqrstuvwxyz\n');
f.seek(10,0)
f.write('HELLO')
f.seek(6, 0)
f.write ('BOO')
f.close()
with open('python2', 'r') as f:
    for line in f:
        print(line, end='')
