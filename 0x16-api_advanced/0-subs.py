#!/usr/bin/python3
"""
Module: 0-subs

Retrieve the number of subscribers for a subreddit using the Reddit API.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a subreddit.

    Args:
        subreddit (str): Name of the subreddit.

    Returns:
        int: Number of subscribers for the subreddit, or 0 if invalid or an error occurs.
    """
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        try:
            subscribers = data['data']['subscribers']
            return subscribers
        except KeyError:
            return 0
    else:
        return 0
