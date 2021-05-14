#  Create a code that do the following in a sequence:
#
#      a) Logs into IG account.
#      b) In every 10 minutes it Check for "followings" account of that IG account
#      c) Figures out new "following" every time on checking.
#      d) Sends a " HI" message to new following, every time it finds new following.
#
# * NOTE: It should send message only once to new following every time,
# shouldn't repeat text to previously texted followings.

# Importing the modules required
import time
from os import remove
from instabot import Bot

# Deleting the cookie json file
remove("C:/Users/91707/PycharmProjects/PythonBot/config/"
       "(enter_d_username)_uuid_and_cookie.json")

# Creating an instance of Bot
bot = Bot()

username = "enter_d_username"
passkey = "enter_d_password"
# Logging in instagram
bot.login(username=username, password=passkey)

# Getting the userid from the username
user_id = bot.get_user_id_from_username(username)

# Getting a list of following users
print("Getting a list of following users")
foll_list = bot.get_user_following(user_id)
print(foll_list)


def send_msg():
    # Creating an empty list for getting the new followers
    new_following = []

    # Getting the updated list of following users
    print("Getting the updated list of following users")
    updated_foll_list = bot.get_user_following(user_id)
    print(updated_foll_list)

    # Finding the new users
    for i in updated_foll_list:
        if i not in foll_list:
            print("Found a new user")
            new_following.append(i)
            foll_list.append(i)

    # Sending msg to new following users
    for user_id2 in new_following:
        print("Sending msg")
        bot.send_message("HI", user_id2)


while True:
    send_msg()
    print("Sleeping for 10 minutes")
    # after every 10 minutes re-running the function
    time.sleep(600)
