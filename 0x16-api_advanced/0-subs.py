#!/usr/bin/python3
""" This a module that uses the Reddit API to make API calls to its Endpoint
"""

import requests


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "phurhard"}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        return data["data"]["subscribers"]
    except Exception as e:
        return 0
