import getpass
from account import Account
from followers import Followers

def main():
    print('Please log in to your Instagram account (\'q\' to quit): ')
    while True:
        username = input('Enter your Instagram username: ')
        if username == 'q':
            quit()
        password = getpass.getpass('Enter your password: ')
        if password == 'q':
            quit()
        account = Account(username, password)
        if account.profile:
            break
    print('Calculating followers, this could take a while... ')
    followers = Followers(account.get_followers(), account.get_followees())
    commands = {
        '1': ('Show users who don\'t follow you back', followers.show_unfollowed),
        '2': ('Show users you don\'t follow back', followers.show_non_followers),
    }
    print('Available commands: ')
    for key, value in commands.items():
        print(f'{key}: {value[0]}')
    while True:
        user_input = input('Choose an option (\'q\' to quit): ')
        if user_input in commands:
            command = commands[user_input][1]
            command()
        elif user_input == 'q':
            quit()
        else:
            print('Invalid command!')


if __name__ == '__main__':
    main()
