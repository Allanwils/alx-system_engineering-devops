#!/usr/bin/python3
"""
Function for number_of_subscribers 
"""

import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
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
