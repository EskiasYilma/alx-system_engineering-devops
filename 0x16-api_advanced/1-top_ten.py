#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first\
    10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    queries the Reddit API and prints the titles of the first\
    10 hot posts listed for a given subreddit.
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

    r = requests.get("https://www.reddit.com/r/{}/hot.json"
                     .format(str(subreddit)), headers=headers)
    try:
        dt = r.json().get('data').get('children')
        for i in dt[:10]:
            print(i.get('data').get('title'))
    except Exception:
        return None
