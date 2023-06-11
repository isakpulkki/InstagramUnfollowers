# InstagramUnfollowers

This is a simple Python command-line application that enables you to identify Instagram users who have unfollowed you and users you don't follow back. 

The application utilizes the [InstaLoader](https://instaloader.github.io/) API to establish communication with Instagram's platform. It's important to note that the current version of InstaLoader does not support 2FA, therefore in order to use this application it is necessary to disable 2FA authentication on your Instagram account.

## Instructions

To run this application, you must have Python3 and [Poetry](https://python-poetry.org) installed.

```bash
# Install dependencies
$ poetry install

# Run the application
$ poetry run invoke start
```

