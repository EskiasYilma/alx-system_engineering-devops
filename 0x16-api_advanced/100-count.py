#!/usr/bin/python3
"""
Module for reddit api
"""
import requests


def print_sorted(hot_list, wordlist):
    """
    matches and prints out sorted list
    """
    if hot_list != []:
        wd = {}

        wordlist = [x.lower() for x in wordlist]
        for i in wordlist:
            wd[i] = 0

        for i in wordlist:
            for j in hot_list:
                for k in str(j).lower().split():
                    if str(i) == str(k):
                        wd[i] += 1
        sorted_hot = sorted(wd.items(), key=lambda v: (v[1], v[0]),
                            reverse=True)
        for i in sorted_hot:
            if i[1] != 0:
                print("{}: {}".format(i[0], i[1]))


def count_words(subreddit, wordlist, hot_list=[], after=None, count=0):
    """
    A recursive function that queries the Reddit API, parses \
    the title of all hot articles, and prints a sorted count \
    of given keywords (case-insensitive, delimited by spaces.
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
                     .format(str(subreddit), "hot", 100,
                             count, after if after else ''),
                     headers=headers,
                     allow_redirects=False)
    try:
        dt = r.json().get('data').get('children')
        for x in dt:
            hot_list.append(x.get('data').get('title'))
        after = r.json().get('data').get('after')
        count += len(dt)
        if after:
            count_words(subreddit, wordlist, hot_list, after, count)
        else:
            print_sorted(hot_list, wordlist)
    except Exception:
        return
