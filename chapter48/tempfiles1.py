import tempfile

print('tempfile.gettempdir():', tempfile.gettempdir())

temp = tempfile.TemporaryFile('w+')
print('temp.name:', temp.name)
print('temp.mode:', temp.mode)

temp.write('Hello world!')
temp.seek(0)
line = temp.readline()
print('line:', line)

