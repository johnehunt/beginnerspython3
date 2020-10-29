from collections import defaultdict

destinations = defaultdict(int)

for city in ['London', 'Cardiff', 'Manchester', 'Edinburgh', 'Dublin', 'London', 'Cardiff', 'London']:
    destinations[city] += 1

print(destinations)
print("destinations['London']", destinations['London'])
print("destinations['Bath']", destinations['Bath'])