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
        for post in data.get('data').get('children')[:10]:
            title = post('data')('title')
            print(title)
    except Exception as e:
        print(f"None {e}")
