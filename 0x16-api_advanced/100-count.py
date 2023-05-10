#!/usr/bin/python3
"""
This module contains a function that performs a recursive query of the Reddit API and sorts the count of given keywords.
"""

import requests


def count_words(subreddit: str, word_list: list, after: str = None, word_count: dict = {}) -> None:
    """
    Recursively queries the Reddit API for the given subreddit,
    parses the title of all hot articles, and prints a sorted count
    of given keywords (case-insensitive, delimited by spaces).

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): A list of keywords to count.
        after (str): A token used to fetch the next page of results.
        word_count (dict): A dictionary used to keep track of the counts
                           for each keyword.

    Returns:
        None.
    """

    if not word_list:
        # base case: no more words to count
        sorted_word_count = sorted(
            word_count.items(),
            key=lambda x: (-x[1], x[0])
        )

        for word, count in sorted_word_count:
            print(f"{word}: {count}")
        return

    # pop the next word from the list
    word = word_list.pop().lower()

    # fetch the hot articles from the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0",
               "Author": "Allanwils",
               "Version": "1.0"
              }
    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        # parse the titles of the hot articles
        data = response.json()["data"]
        after = data["after"]

        for child in data["children"]:
            title = child["data"]["title"].lower()
            count = title.count(word)
            if count:
                # update the count for the word
                if word in word_count:
                    word_count[word] += count
                else:
                    word_count[word] = count

        # call the function recursively with the next word and the
        # updated word count dictionary
        count_words(subreddit, word_list, after, word_count)
    else:
        print(f"Error: failed to fetch data from {url}.")


if __name__ == "__main__":
    count_words("programming", ["Python", "Java", "C++"])
