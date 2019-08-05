import string

# Initialise the template with variables that
# will be substitute with actual values
template = string.Template('$artist sang $song in $year')

# Replace substitute variables with actual value
# Can use a key : value pair that indicates the values to replace
print(template.substitute(artist='Freddie Mercury', song='The Great Pretender', year=1987))
print(template.substitute(artist='Ed Sheeran', song='Galway Girl', year=2017))
print(template.substitute(artist='Camila Cabello', song='Havana', year=2018))

# Using a dictionary to provide the value for the template variables
d = dict(artist = 'Billy Idol', song='Eyes Without a Face', year = 1984)
print(template.substitute(d))

# Optionally providing only some of the template variable values
# print(template.substitute(artist='David Bowie', song='Rebel Rebel'))
print(template.safe_substitute(artist='David Bowie', song='Rebel Rebel'))