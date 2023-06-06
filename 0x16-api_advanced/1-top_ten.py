#!/usr/bin/python3
'''Prints top ten hot post for a given subreddit'''

import requests


def top_ten(subreddit):
    '''Top ten titles in a subreddit'''
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "phurhard"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Raise an exception if the request was not successful
        data = response.json()  # Parse the response JSON data
        if res.status_code != 200:
            return None
        for post in data['data']['children'][:10]:
            title = post['data']['title']
            print(title)
    except requests.exceptions.RequestException as e:
        return None
