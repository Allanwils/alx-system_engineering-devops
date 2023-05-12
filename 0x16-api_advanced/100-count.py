#!/usr/bin/python3
"""
This module provides a function to count the occurrences of a given list of words in the titles of hot posts in a given subreddit.

Functions:
- count_words(subreddit: str, word_list: List[str], found_list: Optional[List[str]] = [], after: Optional[str] = None) -> None
"""

import requests
from typing import List, Optional

def count_words(subreddit: str, word_list: List[str], found_list: Optional[List[str]] = [], after: Optional[str] = None) -> None:
    """
    Count the occurrences of a given list of words in the titles of hot posts in a given subreddit.

    Args:
    - subreddit (str): The subreddit to search for hot posts.
    - word_list (List[str]): A list of words to search for in the titles of hot posts.
    - found_list (Optional[List[str]]): A list of words that have already been found in the titles of hot posts.
    - after (Optional[str]): The ID of the last post in the previous request. Used to paginate through the results.

    Returns:
    - None: The function prints the result to the console.

    Raises:
    - None.

    Example:
    >>> count_words("news", ["trump", "biden", "election"])
    trump: 5
    election: 3
    biden: 2
    """
    user_agent = {'User-agent': 'test45'}
    posts = requests.get(f"http://www.reddit.com/r/{subreddit}/hot.json?after={after}", headers=user_agent)

    if after is None:
        word_list = [word.lower() for word in word_list]

    if posts.status_code == 200:
        posts = posts.json()['data']
        aft = posts['after']
        posts = posts['children']
        for post in posts:
            title = post['data']['title'].lower()
            for word in title.split(' '):
                if word in word_list:
                    found_list.append(word)
        if aft is not None:
            count_words(subreddit, word_list, found_list, aft)
        else:
            result = {}
            for word in found_list:
                if word.lower() in result.keys():
                    result[word.lower()] += 1
                else:
                    result[word.lower()] = 1
            for key, value in sorted(result.items(), key=lambda item: item[1], reverse=True):
                print(f"{key}: {value}")
    else:
        return
