#!/usr/bin/python3
"""
This module provides a function that recursively returns a list of all hot post titles for a given subreddit.
"""

import requests


def recurse(subreddit: str, hot_list: list = [], after: str = None) -> list:
    """
    Recursively returns a list of all hot post titles for a given subreddit.
    
    :param subreddit: The name of the subreddit.
    :param hot_list: The list of hot post titles. Default is an empty list.
    :param after: A token for pagination. Default is None.
    :return: A list of all hot post titles for the given subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return None
    
    r = requests.get(f'http://www.reddit.com/r/{subreddit}/hot.json',
                     headers={'User-Agent': 'Masiga'},
                     params={'after': after}).json()
    after = r.get('data', {}).get('after', None)
    posts = r.get('data', {}).get('children', None)
    
    if posts is None or (len(posts) > 0 and posts[0].get('kind') != 't3'):
        if len(hot_list) == 0:
            return None
        return hot_list
    else:
        for post in posts:
            hot_list.append(post.get('data', {}).get('title', None))
            
    if after is None:
        if len(hot_list) == 0:
            return None
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
