#!/usr/bin/python3
"""
recur function that querries the api given in task
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    querries the api to get the hottest posts
    """
    res = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"after": after},
    )

    if res.status_code == 200:
        for get_data in res.json().get("data").get("children"):
            data = get_data.get("data")
            title = data.get("title")
            hot_list.append(title)
        later = res.json().get("data").get("after")

        if later is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, later)
    else:
        return None
