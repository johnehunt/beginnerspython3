from collections import Counter

ages = [20, 20, 22, 23, 55, 52, 87, 20, 17, 23, 1, 52, 52]

age_counts = Counter(ages)

print(age_counts.most_common())
print(sum(age_counts.values()))
print(list(age_counts))
