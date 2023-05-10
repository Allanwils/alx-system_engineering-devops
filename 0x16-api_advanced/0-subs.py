#!/usr/bin/python3
"""
This module provides a function for retrieving the number of subscribers for a given subreddit on Reddit.

Function:
number_of_subscribers(subreddit: str) -> int
- Takes a subreddit name as a string parameter.
- Returns the number of subscribers for the given subreddit as an integer.
- If the subreddit does not exist or an error occurs, returns 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for a given subreddit on Reddit.

    Args:
        subreddit (str): The name of the subreddit to retrieve the number of subscribers for.

    Returns:
        int: The number of subscribers for the given subreddit.

    Raises:
        requests.exceptions.HTTPError: If a non-404 HTTP error occurs.
        requests.exceptions.RequestException: If an error occurs while making the request.

    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Python/requests:APIproject:v1.0.0 (by /u/Allanwils)'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_error:
        if response.status_code == 404:
            return 0
        else:
            print(f"HTTP error occurred: {http_error}")
            return 0
    except requests.exceptions.RequestException as error:
        print(f"An error occurred: {error}")
        return 0

    data = response.json()
    if 'data' not in data or 'subscribers' not in data['data']:
        print(f"Invalid response data from Reddit API for subreddit {subreddit}.")
        return 0

    return data['data']['subscribers']
