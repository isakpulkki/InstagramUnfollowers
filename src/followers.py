class Followers:
    def __init__(self, followers: list, followees: list):
        self.followers = [follower for follower in followers]
        self.followed = [followee for followee in followees]
        self.not_followed = self.get_not_followed()
        self.unfollowers = self.get_unfollowers()

    def get_unfollowers(self):
        return [
            followee
            for followee in self.followed
            if followee not in self.followers
        ]

    def get_not_followed(self):
        return [
            follower
            for follower in self.followers
            if follower not in self.followed
        ]

    def show_unfollowed(self):
        self.display_users(self.unfollowers, "user(s) who don't follow you back")

    def show_non_followers(self):
        self.display_users(self.not_followed, "user(s) who you don't follow back")

    def display_users(self, users, message):
        print(f'Found {len(users)} {message}:')
        for user in users:
            print(user)
