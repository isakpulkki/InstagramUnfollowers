import instaloader
from instaloader import TwoFactorAuthRequiredException
from instaloader import InstaloaderException

class Account:

    def __init__(self, username: str, password: str):
        self.username = username
        self.loader = self.login_loader(username, password)
        self.profile = self.get_profile(username)

    def login_loader(self, username: str, password: str):
        loader = instaloader.Instaloader()
        try:
            loader.login(username, password)
        except TwoFactorAuthRequiredException:
            print(
                '2FA does not currently work with the Instaloader API, please disable it.')
            return
        except InstaloaderException:
            print('Something went wrong, check your username and password.')
            return
        return loader

    def get_profile(self, username):
        if self.loader:
            try:
                return instaloader.Profile.from_username(self.loader.context, username)
            except InstaloaderException:
                print('Could not load the profile, quitting...')
                quit()
        return False

    def get_followers(self):
        return self.profile.get_followers()

    def get_followees(self):
        return self.profile.get_followees()
