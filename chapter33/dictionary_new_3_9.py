# New feature added to dictionaries for Python 3.9
# Two union operators, merge | and update |=,
# have been introduced for dict.

offices = {'John': 1, 'Denise' : 21}
labs = {'Cyber' : 5, 'Games': 33}

print('offices', offices)
print('labs', labs)

# Merge two dictionaries to create a new one
all_rooms = offices | labs
print('all_rooms', all_rooms)

# Update one dictionary with contents of another
offices |= labs
print('offices', offices)
