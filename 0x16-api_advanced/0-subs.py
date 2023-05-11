#!/usr/bin/python3
"""
Contains function for the number_of_subscribers

This module provides a function to get the number of subscribers for a given subreddit using the Reddit API.

Note:
    This function relies on the availability and stability of the Reddit API. If the API changes or is unavailable, 
    this function may not work as intended.

If you plan to use this function for commercial or high-traffic purposes, make sure to comply with the Reddit API 
terms of use and follow proper API etiquette, such as adding rate limiting and error handling.
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
