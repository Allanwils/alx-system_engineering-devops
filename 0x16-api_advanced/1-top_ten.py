#!/usr/bin/python3
"""
Function for top_ten posts listed for subreddit
"""

import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Python/requests:APIproject:v1.0.0 (by /u/Allanwils)"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        for post in response.json()["data"]["children"]:
            print(post["data"]["title"])
    else:
        print(None)
