#!/usr/bin/python3
import requests
"""
a function that queries the Reddit API and returns the number\
 of subscribers (not active users, total subscribers) for a \
 given subreddit. If an invalid subreddit is given, the \
 function should return 0.
"""


def number_of_subscribers(subreddit):
    """
    a function that queries the Reddit API and returns the number\
    of subscribers (not active users, total subscribers) for a \
    given subreddit. If an invalid subreddit is given, the \
    function should return 0.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:113.0) \
                       Gecko/20100101 Firefox/113.0',
    }

    r = requests.get('https://reddit.com/r/' + subreddit + '/about/.json', headers=headers)
    try:
        return (r.json().get('data').get('subscribers'))
    except Exception:
        return (0)
