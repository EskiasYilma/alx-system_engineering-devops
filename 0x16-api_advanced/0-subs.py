#!/usr/bin/python3
"""
a function that queries the Reddit API and returns the number\
 of subscribers (not active users, total subscribers) for a \
 given subreddit. If an invalid subreddit is given, the \
 function should return 0.
"""
import requests


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
        'Accept': 'text/html,application/xhtml+xml,application/xml;\
                   q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'DNT': '1',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    r = requests.get("https://www.reddit.com/r/{}/about.json"
                     .format(str(subreddit)), headers=headers)
    try:
        return (r.json().get('data').get('subscribers'))
    except Exception:
        return (0)
