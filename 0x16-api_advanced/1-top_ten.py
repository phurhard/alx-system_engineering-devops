#!/usr/bin/python3
""" A module to make API calls to Reddit API endpoints
"""

import requests


def top_ten(subreddit):
    """ Returns a list of to ten titles in the hot list of a subreddit
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "phurhard"}

    try:
        res = requests.get(url, headers=headers)
        data = res.json()

        children = data.get('data').get('children')
        for post in children:
            print(post.get('data').get('title'))
    except Exception as e:
        print("None")
