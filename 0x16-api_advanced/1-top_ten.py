#!/usr/bin/python3
"""
gets top 10 trending posts from reddit on code 200
"""

import requests


def top_ten(subreddit):
    """
    querries the api
    """
    res = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"limit": 10}
    )
    if res.status_code == 200:
        for get_data in res.json().get("data").get("children"):
            data = get_data.get("data")
            title = data.get("title")
            print(title)
    else:
        print(None)
