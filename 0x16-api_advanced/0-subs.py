#!/usr/bin/python3
""" This is an api call function
that uses the reddit api endpoints to make calls
"""
import requests

redirect = [301, 302]

def number_of_subscribers(subreddit):
    """ Returns the number of subscribers for the given subreddit"""
    api = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {"User-Agent": "phurhard"}

    res = requests.get(api, allow_redirects=False, headers=headers)
    res.raise_for_status()
    if res.status_code in redirect:
        '''check if redirect'''
        
        return 0
    else:
        response = res.json()
        subscriber = response['data']['subscribers']
        return subscriber
