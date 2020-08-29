print('Welcome to the Database Admin App')

creds = {
    'admin': 'admin123',
    'bill87': 'ahens010101',
    'ann557': 'hulu1222333',
    'gogi101': 'rockstar007'
}
repeat = True
while repeat:
    uname = input('Enter your Username: ').strip()
    if uname in creds.keys():
        passwd = input(f'Hi {uname.title()}, Enter your Password: ').strip()
        if passwd == creds[uname]:

            if uname == 'admin':
                print(f'Hello {uname}, You are logged in as Administrator..!\nHere is your current user database.')
                for k, v in creds.items():
                    print(f'Username:{k}, Password:{v}')
                print('The App will exit now.Until next time. Good bye.')
                input('Press Enter to exit.')
                repeat = False
            else:
                print(f'Hello {uname}, You are logged in ..!')
                change_pass = input('Would you like to change your password today? ').lower() \
                    .strip()
                if change_pass.startswith('y'):
                    new_pwd = str(input('Enter a new password(min 8 chars): '))
                    if len(new_pwd) >= 8:
                        creds[uname] = new_pwd
                        print(f'{uname} your password has been renamed to: {creds[uname]}.The App will exit now.Until'
                              f' next time. Good bye.')
                        input('Press Enter to exit.')
                        repeat = False
                    else:
                        print(f'New password is not 8 chars long.\n{uname.title()} your password'
                              f' remains the same as current:{creds[uname]}. The App will exit now.Until next time. '
                              f'Good bye.')
                        input('Press Enter to exit.')
                        repeat = False
                else:
                    print('Your password has not been updated.The App will exit now.Until next time. Good bye.')
                    input('Press Enter to exit.')
                    repeat = False
        else:
            choice = input('Incorrect password. Would you like to try again,(y/n):')
            if choice.startswith('n'):
                print('The App will exit now. Good bye.')
                input('Press Enter to exit.')
                repeat = False
    else:
        retry = input('Incorrect Username.You want to try again?(y/n): ')
        if retry.startswith('n'):
            print('The App will exit now. Good bye.')
            input('Press Enter to exit.')
            repeat = False
