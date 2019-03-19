from collections import Counter, OrderedDict

word_count = Counter()

input_string = input('Please enter text to be analysed:')


words_in_string = input_string.split(' ')
for word in words_in_string:
    if word == '':
        pass  # Do nothing
    elif word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print('Unordered Counter')
print(word_count)

ordered_word_count = OrderedDict()
for key in sorted(word_count):
    ordered_word_count[key] = word_count[key]

print('Ordered Word Count')
print(ordered_word_count)

