print('Welcome to Frequency Analysis App.')

text = input('Enter a message you want to code: ')

coded_msg = []
decoded = []

for letter in text:
    asciCode = (ord(letter)) + 1
    chrCode = chr(asciCode)
    coded_msg.append(chrCode)
print(f'The coded message is: ')
for i in coded_msg:
    print(i, end='')

choice = input("\nDo you want to see your original message?(Yes/No) ").lower().strip()
if choice.startswith('y'):
    for lett in coded_msg:
        asciCode = (ord(lett)) - 1
        chrCode = chr(asciCode)
        decoded.append(chrCode)
    print('Your original text was: ')
    for i in decoded:
        print(i, end='')
print('\nThank you for using the Code breakers App')
