#!/usr/bin/python3
"""
This module provides a function to query the Reddit API and return the number of subscribers
for a given subreddit. If the subreddit is invalid or an error occurs, the function returns 0.

The module does not require authentication for querying the Reddit API, but it sets a custom
User-Agent to avoid issues with rate limiting and request blocking.

Example usage:

    from number_of_subscribers import number_of_subscribers
    
    print(number_of_subscribers("python"))  # Outputs the number of subscribers for r/python
    print(number_of_subscribers("nonexistingsubreddit12345"))  # Outputs 0 for a non-existing subreddit

Function:
    - number_of_subscribers(subreddit)
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to get the number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
    
    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid or an error occurs.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'my_reddit_bot/0.1 by your_username'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0


# Example usage:
if __name__ == "__main__":
    print(number_of_subscribers("python"))  # Outputs the number of subscribers for r/python
    print(number_of_subscribers("nonexistingsubreddit12345"))  # Outputs 0 for a non-existing subreddit
