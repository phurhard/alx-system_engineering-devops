#!/usr/bin/python
""" A module for sending requests to Reddit API endpoints
"""
import requests


def recurse(subreddit, hot_list=[]):
    """ Uses recursion to print out all the
    titles in the hot section for a given subreddit
    """
    headers = {"User-Agent": "phurhard"}

    try:
        if not hot_list:
            url = "https://www.reddit.com/r/{}/hot.json?\
            limit=25".format(subreddit)
        else:
            last_post = hot_list[-1]
            after = last_post['data']['name']
            url = "https://ww.reddit.com/r/{}/hot.json?\
            limit=25&after={}".format(subreddit, after)
        res = requests.get(url, headers=headers)
        data = res.json()
        posts = data['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])
        after = data['data']['after']
        print(len(hot_list))
        if after:
            recurse(subreddit, hot_list)
            print('After each recurse: {}'.format(len(hot_list)))
#        return hot_list
    except Exception as e:
        return None
