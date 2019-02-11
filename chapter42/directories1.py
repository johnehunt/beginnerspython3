import os

print('os.getcwd(:', os.getcwd())
print('List contents of directory')
print(os.listdir())

print('Create mydir')
os.mkdir('mydir')
print('List the updated contents of directory')
print(os.listdir())

print('Change into mydir directory')
os.chdir('mydir')
print('os.getcwd(:', os.getcwd())

print('Change back to parent directory')
os.chdir('..')
print('os.getcwd(:', os.getcwd())

print('Remove mydir directory')
os.rmdir('mydir')
print('List the resulting contents of directory')
print(os.listdir())

