#!/usr/bin/python3

"""
This module contains the function top_ten, which can be used to print the titles
of the top ten hot posts for a given subreddit.

"""

import requests


def top_ten(subreddit):
    """
    This function prints the titles of the top ten hot posts for a given subreddit.

    Args:
        subreddit (str): A string representing the subreddit whose top ten hot posts
        need to be printed.

    Returns:
        None: Prints the titles of the top ten hot posts for the given subreddit, or
        None if the subreddit is invalid or there are no hot posts available.
    """

    # Check if subreddit is a valid string
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    # Make a request to get the top ten hot posts for the given subreddit
    r = requests.get('http://www.reddit.com/r/{}/hot.json'.format(subreddit),
                     headers={'User-Agent': 'Python/requests:APIproject:v1.0.0 (by /u/Masiga)'},
                     params={'limit': 10}).json()

    # Check if the request was successful and get the list of posts
    posts = r.get('data', {}).get('children', None)

    # Check if there are no hot posts available for the given subreddit
    if posts is None or (len(posts) > 0 and posts[0].get('kind') != 't3'):
        print(None)
        return

    # Print the titles of the top ten hot posts for the given subreddit
    for post in posts:
        print(post.get('data', {}).get('title', None))
