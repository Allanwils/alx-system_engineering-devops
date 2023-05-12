#!/usr/bin/python3

"""
Module: reddit_scraper

This module provides a function `recurse` to scrape all hot post titles for a given subreddit using Reddit API.

Functions:
    - recurse(subreddit: str, hot_list: Optional[List[str]] = [], after: Optional[str] = None) -> Optional[List[str]]:
        Scrapes all the hot post titles for a given subreddit.

        Parameters:
            - subreddit: Name of the subreddit to scrape.
            - hot_list (Optional): List to store the hot post titles.
            - after (Optional): A token that helps in paginating through the posts.

        Returns:
            - A list of all hot post titles for the given subreddit. If the subreddit name is invalid, the function returns None.
"""

import requests
from typing import List, Optional


def recurse(subreddit: str, hot_list: Optional[List[str]] = [], after: Optional[str] = None) -> Optional[List[str]]:
    """Returns a list of all hot post titles for a given subreddit."""
    if subreddit is None or type(subreddit) is not str:
        return None
    r = requests.get('http://www.reddit.com/r/{}/hot.json'.format(subreddit),
                     headers={'User-Agent': 'Python/requests:APIproject:v1.0.0 (by /u/Masiga)'},
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
