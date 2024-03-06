#!/usr/bin/python3
"""
gets the subs from a sub redit on code 200
"""

import requests



def number_of_subscribers(subreddit):
    """gets sub numner from  a sub reddit"""
    uri = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(uri, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        data = res.json()
        subs = data['data']['subscribers']
        return subs
    else:
        return 0
