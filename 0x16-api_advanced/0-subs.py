#!/usr/bin/python3
""" A module which makes API calls to the Reddit API endpoints
and using the response for further manipulation:
"""
import requests


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers for the given subreddit"""
    api = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {"User-Agent": "phurhard"}

    try:
        res = requests.get(api, headers=headers)
        response = res.json()
        subscr = response['data']['subscribers']
        return subscr
    except Exception:
        return 0
