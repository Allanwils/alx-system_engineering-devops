#!/usr/bin/python3
"""
Contains function for the number_of_subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """
    This function takes a string argument representing a subreddit, and returns the number of subscribers for that subreddit.

    Args:
        subreddit (str): The name of the subreddit for which to get the number of subscribers.

    Returns:
        int: The number of subscribers for the given subreddit.

        If the subreddit is None or not a string, the function returns 0.
    """

    if subreddit is None or type(subreddit) is not str:
        return 0
    r = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': 'Masiga'}).json()
    subs = r.get("data", {}).get("subscribers", 0)
    return subs
