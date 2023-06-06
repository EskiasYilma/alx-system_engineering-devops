#!/usr/bin/python3
"""
Module for reddit api
"""
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """
    A recursive function that queries the Reddit API and returns \
    a list containing the titles of all hot articles for a \
    given subreddit. If no results are found for the \
    given subreddit, the function should return None.
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

    r = requests.get("https://www.reddit.com/r/{}/.json?sort={}\
                      &limit={}&count={}&after={}"
                     .format(str(subreddit), "hot", 100, count, after),
                     headers=headers)
    dt = r.json().get('data').get('children')
    after = r.json().get('data').get('after')
    try:
        dt = r.json().get('data').get('children')
        for x in dt:
            hot_list.append(x['data']['title'])
        after = r.json().get('data').get('after')
        count += len(dt)
        if after:
            recurse(subreddit, hot_list, after, count)

        return hot_list
    except Exception:
        return None
