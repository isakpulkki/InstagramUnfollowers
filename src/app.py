import getpass
from account import Account
from followers import Followers

def prompt_login(account):
    while True:
        username = input('Enter your Instagram username: ')
        if username == 'q':
            quit()
        password = getpass.getpass('Enter your password: ')
        if password == 'q':
            quit()
        account.login_client(username, password)
        if account.key:
            break

def display_commands(commands):
    print('Available commands: ')
    for key, value in commands.items():
        print(f'{key}: {value[0]}')

def handle_user_input(commands):
    while True:
        user_input = input('Choose an option (\'q\' to quit): ')
        if user_input in commands:
            command = commands[user_input][1]
            command()
        elif user_input == 'q':
            quit()
        else:
            print('Invalid command!')

def main():
    print('Please log in to your Instagram account (\'q\' to quit): ')
    account = Account()
    if account.key is None:
        prompt_login(account)
    
    print('Calculating unfollowers, this could take a while.')
    followers = Followers(account.get_followers(), account.get_followees())

    commands = {
        '1': ('Show users who don\'t follow you back', followers.show_unfollowed),
        '2': ('Show users you don\'t follow back', followers.show_non_followers),
    }
    
    display_commands(commands)
    handle_user_input(commands)

if __name__ == '__main__':
    main()