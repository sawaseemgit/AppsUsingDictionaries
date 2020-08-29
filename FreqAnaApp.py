from collections import Counter

print('Welcome to Frequency Analysis App.')
freq = {
}
non_letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '.', '?',
               '/', '\\', '!', '\'', '\"', '@', '#', '$', '%', '&', '*', ';']
text = input('Enter a word or a phrase to count the occurrence of each letter: ') \
    .lower().strip()
for nl in non_letters:
    text = text.replace(nl, '')

for letter in text:
    if letter in freq.keys():
        freq[letter] += 1
    else:
        freq[letter] = 1

total = len(text)
print('Letter\t\tOccurrence\tPercentage%')

for k, v in sorted(freq.items()):
    print(f'{k}\t\t{v}\t\t{round((100 * v / total), 2)}')

# print('Letters ordered from highest occurrence to lowest:')
unordered_list = Counter(text)
ordered_list = unordered_list.most_common()
ordered_list_key = []
for pair in ordered_list:
    ordered_list_key.append(pair[0])

print(f'Letters ordered from highest occurrence to lowest:')
for letter in ordered_list_key:
    print(letter, end='')
