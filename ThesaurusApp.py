import random as r

print('Welcome to the Thesaurus App')

thesaurus = {
    'hot': ['balmy', 'summery', 'tropical', 'boiling', 'scorching'],
    'cold': ['chilly', 'cool', 'polar', 'frigid', 'freezing'],
    'sad': ['unhappy', 'downcast', 'miserable', 'glum', 'melancholy'],
    'happy': ['content', 'cheery', 'merry', 'jovial', 'jocular']
}
print(f'Choose a word from the below words whose thesaurus you want:\n')
for key in thesaurus:
    print(f'\t-{key}')
word = input('Enter your word: ').lower().strip()
if word in thesaurus.keys():
    index = r.randint(0, 4)
    synword = thesaurus[word][index]
    print(f'The synonym for {word} is {synword}.')
else:
    print('Sorry that word isnt in the thesaurus currently')

response = input('Would you like to see all of the thesaurus present:(y/n) ') \
    .lower().strip()
if response.startswith('y'):
    for k, v in thesaurus.items():
        print(f'The synonyms for {k.title()} are:')
        for values in v:
            print(f'\t-{values}')
else:
    print('Hope you enjoyed the App.')
