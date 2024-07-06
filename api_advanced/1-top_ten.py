#!/usr/bin/python3
"""Return 10 hot posts listed for a given subreddit."""

import requests


def top_ten(subreddit):
    """Start"""
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}
    try:
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)
        HOT_POSTS = RESPONSE.json().get("data").get("children")
        [print(post.get('data').get('title')) for post in HOT_POSTS]
    except Exception:
        print(None)
