print('Welcome to Yes/No polling App')
poll = {
    'passwd': 'acc',
}
yes = 0
no = 0
issue = input('What is the Yes/No issue you will be voting on today: ').strip()
no_voters = int(input('What is number of voters you want to allow: '))

repeat = True
while repeat:

    for i in range(no_voters):
        fname = input('What is your full name: ').title().strip()
        if fname in poll.keys():
            print('Sorry, you seem to have already voted.')
        else:
            print(f"Hii {fname}, Today's issue is: {issue}")
            choice = input('What is your vote (yes/no): ').lower().strip()
            if choice.startswith('y'):
                yes += 1
            elif choice.startswith('n'):
                no += 1
            else:
                print('Thats an invalid answer.')
            poll[fname] = choice
            print(f'Thank you {fname}. Your vote {poll[fname]} has been recorded.')
        if i == (no_voters - 1):
            repeat = False
total = len(poll.keys())
print(f'The following {total} people voted: ')
for key in poll.keys():
    print(key)
print(f'On the following issue: {issue}')
if yes > no:
    print(f'Yes wins. {yes} votes to {no}.')
elif yes < no:
    print(f'No wins. {no} votes to {yes}.')
else:
    print(f'It was a tie. {yes} votes to {no}.')

passwd = str(input('To see all of the voting results, enter admin password: '))\
    .strip()
if passwd == poll['passwd']:
    for k, v in poll.items():
        print(f'Voter:{k}   Vote:{v}')
else:
    print('Incorrect password. Good bye.. ')

print("Thank you for using the Yes/no App.")
