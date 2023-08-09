#!/usr/bin/python3
"""
Module: 2-recurse

Fetches titles of hot Reddit articles for a subreddit recursively
and handles pagination.
"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    Recursively retrieve the titles of all hot articles for a subreddit.

    Args:
        subreddit (str): Name of the subreddit.
        hot_list (list): List to store the titles (default is an empty list).

    Returns:
        list: List containing the titles of all hot articles for the subreddit,
              or None if the subreddit is invalid or no results are found.
    """
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'limit': 100}

    if hot_list:
        after = hot_list[-1].get('data', {}).get('name')
        if after:
            params['after'] = after

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        posts = data.get('children', [])
        if posts:
            hot_list.extend(posts)
            return recurse(subreddit, hot_list=hot_list)
        else:
            return hot_list
    else:
        return None
