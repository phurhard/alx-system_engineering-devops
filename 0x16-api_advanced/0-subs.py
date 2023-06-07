#!/usr/bin/python3
""" A module to make API calls to Reddit API endpoints and use the response
to complete different tasks."""
import requests

redirect = [301, 302]


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers for the given subreddit"""
    api = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {"User-Agent": "phurhard"}

    try:
        res = requests.get(api, headers=headers)
        response = res.json()
        subscr = response.get('data').get('subscribers')
        return subscr
    except Exception:
        return 0
