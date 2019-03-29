import re

s = 'Hello \n world'
print(s)

s = r'Hello \n world'
print(s)

text1 = 'john williams'
pattern = '[Jj]ohn'
print('looking in', text1, 'for the pattern', pattern)
if re.search(pattern, text1, re.MULTILINE):
    print('Match has been found')

line1 = 'The price is 23.55'
containsIntegers = r'\d+'
if re.search(containsIntegers, line1):
    print('Line 1 contains an integer')
else:
    print('Line 1 does not contain an integer')

rePattern = re.compile(containsIntegers)
matchLine1 = rePattern.search(line1)
if matchLine1:
    print('Line 1 contains a number')
else:
    print('Line 1 does not contain a number')

print('-' * 10)

matchLine1 = re.search(containsIntegers, line1)
if matchLine1:
    print('Line 1 contains a number')
else:
    print('Line 1 does not contain a number')

# Alternative words
music = r'Beatles|Adele|Gorillaz'
request = 'Play some Adele'
if re.search(music, request):
    print('Set Fire to the Rain')
else:
    print('No Adele Available')

music2 = r'A (song|ballad|ditty) from (Paloma|Adele)'
request = 'A ditty from Paloma'
if re.search(music2, request):
    print('Only Love Can Hurt like this')

line = 'root:*:0:0:System Administrator:/var/root:/bin/sh'
rootUser = r'root:'
if re.search(rootUser, line):
    print('Root')
else:
    print('Not root')

usesSh = r'/bin/sh$'
if re.search(usesSh, line):
    print('sh')
else:
    print('Some other shell')

name = 'John Smith'
nameRe = r'john'
if re.search(nameRe, name, re.IGNORECASE):
    print('Match')

sound = r'boink+'
if re.search(sound, 'boink'):
    print('boink matches')
if re.search(sound, 'boinkkkk'):
    print('boinkkkk matches')

sound = r'(boink)+'
if re.search(sound, 'boink'):
    print('boink matches')
if re.search(sound, 'boinkboink'):
    print('boinkboink matches')

inputStr = '123-44-7890'
if re.search(r'\d{3}-\d{2,4}-\d{4,8}', inputStr):
    print('Input Matches')
else:
    print('Input Does Not Match')

components = r'(\D+)(\d+)(\D+)(\d+)'
inputText = 'abcd123defg 456 '
match_results = re.search(components, inputText)
captureGroups = match_results.groups()
for group in captureGroups:
    print(group, '; ', end='')
print()

p = re.compile(r'\W+')
s = '20 High Street'
print(p.split(s))

pattern = '(England|Wales|Scotland)'
input = 'England for football, Wales for Rugby and Scotland for the Highland games'

print(re.sub(pattern, 'England', input))
print(re.subn(pattern, 'Scotland', input))
x = re.sub(pattern, 'Wales', input, 2)
print(x)

str = 'The rain in Spain stays mainly on the plain'
results = re.findall('[a-zA-Z]{2}ai.', str)
print(results)
for s in results:
    print(s)

str = 'It was a hot summer night'
x = re.split('\s', str)
print(x)
