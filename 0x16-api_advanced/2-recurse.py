#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a sudreddit list
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive function that queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit. If no results are found
    for the given subreddit, the function should return None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Python/requests:APIproject:v1.0.0 (by /u/Allanwils)'}

    # If after parameter is not None, add it to the URL
    if after:
        url += f"?after={after}"

    response = requests.get(url, headers=headers)

    # Check if subreddit exists
    if response.status_code != 200:
        return None

    data = response.json()['data']

    # Add titles to hot_list
    for child in data['children']:
        hot_list.append(child['data']['title'])

    # If there is a next page, recursively call recurse() with the after parameter
    if data['after']:
        recurse(subreddit, hot_list, after=data['after'])

    return hot_list
