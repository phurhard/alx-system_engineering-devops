<<<<<<< HEAD
#!/usr/bin/python3
""" A module that has a a recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles for a given
subreddit. If no results are found for the given subreddit, the function
should return None
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """ A recursive function that queries the Reddit API and returns a
    list containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, the function should
    return None.
    """
    if hot_list is None:
        hot_list = []
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {
            "limit": 100,
            "raw_json": 1,
            "after": after
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110\
        Safari/537.3"
    }
    response = requests.get(url, params=params, headers=headers,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = (data['data']['children'])
        if not posts:
            return hot_list

        for post in posts:
            hot_list.append(post['data']['title'])
        after = data['data']['after']
        if after:
            return recurse(subreddit, hot_list=hot_list, after=after)
        else:
            return (hot_list)
    else:
        return (None)
=======
#!/usr/bin/python
""" A module for sending requests to Reddit API endpoints
"""

import requests


def recurse(subreddit, hot_list=[]):
    """ Uses recursion to print out all the titles in the hot section for a given subreddit
    """
    
    headers = {"User-Agent": "phurhard"}

    try:
        if not hot_list:
            url = "https://www.reddit.com/r/{}/hot.json?limit=25".format(subreddit)
        else:
            last_post = hot_list[-1]
            after = last_post['data']['name']
            url = "https://ww.reddit.com/r/{}/hot.json?limit=25&after={}".format(subreddit, after)
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
>>>>>>> a793971a290eddd62e079676fde38c21160bca4f
