#!/usr/bin/python3
"""
Module: 1-top_ten

This script queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts for a subreddit.

    Args:
        subreddit (str): Name of the subreddit.

    Returns:
        None
    """
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        try:
            posts = data['data']['children'][:10]
            for post in posts:
                title = post['data']['title']
                print(title)
        except KeyError:
            print("None")
    else:
        print("None")
