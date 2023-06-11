class Followers:
    def __init__(self, followers: list, followees: list):
        self.followers = [follower.username for follower in followers]
        self.followed = [followee.username for followee in followees]
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
        print(
            f'Found {len(self.unfollowers)} user(s) who don\'t follow you back: ')
        for unfollower in self.unfollowers:
            print(unfollower)

    def show_non_followers(self):
        print(
            f'Found {len(self.not_followed)} user(s) who you don\'t follow back: ')
        for follower in self.not_followed:
            print(follower)
