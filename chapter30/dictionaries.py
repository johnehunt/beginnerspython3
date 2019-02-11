cities = {'Wales': 'Cardiff',
          'England': 'London',
          'Scotland': 'Edinburgh',
          'Northern Ireland': 'Belfast',
          'Ireland': 'Dublin'}

print(len(cities))
print(cities)
print('cities[Wales]:', cities['Wales'])
print('cities.get(Ireland):', cities.get('Ireland'))

print(cities.values())
print(cities.keys())
print(cities.items())

print('Wales' in cities)
print('France' not in cities)

for country in cities:
    print(country, end=', ')
    print(cities[country])

cities['Wales'] = 'Swansea'
print(cities)
cities.clear()
print(cities)

cities = {'Wales': 'Cardiff',
          'England': 'London',
          'Scotland': 'Edinburgh',
          'Northern Ireland': 'Belfast',
          'Ireland': 'Dublin'}
print(cities)
cities.popitem()
print(cities)
cities.pop('Northern Ireland')
print(cities)
del cities['Scotland']
print(cities)

print('-' * 25)

d = {'one': 1, 'two': 2}
print(d)
print(type(d))
print(d['two'])
d['three'] = 3
print(d)
del d['two']
print(d)

seasons = {"Spring": ('Mar', 'Apr', 'May'),
           'Summer': ('June', 'July', 'August'),
           'Autumn': ('September', 'October', 'November'),
           "Winter": ('December', 'January', 'February')}
print(seasons["Spring"])
print(seasons["Spring"][1])

print('-' * 25)

print(d.keys())
print(d.values())
values = d.values()
for e in values:
    print(e)

print(d.items())

d['four'] = 4
print(d.keys())
print(sorted(d.keys()))
