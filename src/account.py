from instagrapi import Client
from instagrapi.exceptions import BadPassword, TwoFactorRequired
import os

SESSION_FILE = "session.json"

class Account:
    def __init__(self):
        self.client = Client()
        self.key = None
        self.load_session()

    def load_session(self):
        if os.path.exists(SESSION_FILE):
            try:
                print("Attempting to load saved session...")
                self.client.load_settings(SESSION_FILE)
                self.client.login('...', '...')
                print("Session loaded successfully!")
                self.key = self.client.account_info().model_dump()["pk"]
            except Exception as e:
                print(f"Failed to load session. Proceeding with login...")

    def login_client(self, username: str = None, password: str = None):
        if username and password:
            try:
                self.client.login(username, password)
                self.client.dump_settings(SESSION_FILE)
                self.key = self.client.account_info().model_dump()["pk"]
                print("Successfully logged in!")
            except TwoFactorRequired:
                self.handle_two_factor_auth(username, password)
            except BadPassword:
                print("Incorrect password.")
            except Exception:
                print(f"Could not log in! Check your username.")

    def handle_two_factor_auth(self, username, password):
        print("Two-factor authentication is required.")
        verification_code = input("Enter the 2FA code: ")
        if verification_code == 'q':
            quit()
        try:
            self.client.login(username=username, password=password, verification_code=verification_code)
            self.key = self.client.account_info().model_dump()["pk"]
            self.client.dump_settings(SESSION_FILE)
            print("Successfully logged in!")
        except Exception as e:
            print(f"Could not log in! Check your 2FA code.")

    def get_followers(self):
        if self.key:
            try:
                print('Retrieving followers...')
                followers_data = self.client.user_followers(self.key)
                return [follower.username for follower in followers_data.values()]
            except Exception:
                print(f"Could not retrieve the followers.")
        return []

    def get_followees(self):
        if self.key:
            try:
                print('Retrieving followees...')
                followees_data = self.client.user_following(self.key)
                return [followee.username for followee in followees_data.values()]
            except Exception:
                print(f"Could not retrieve the followees.")
        return []