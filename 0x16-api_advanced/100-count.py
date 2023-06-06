#!/usr/bin/python3
"""
A recursive function that queries the Reddit API, parses \
the title of all hot articles, and prints a sorted count \
of given keywords (case-insensitive, delimited by spaces.
"""
import requests


def count_words(subreddit, word_list, hot_list=[], after=None, count=0):
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
            count_words(subreddit, word_list, hot_list, after, count)
        else:
            wd = {}
            word_list = [x.lower() for x in word_list]
            for i in word_list:
                wd[i] = 0

            for i in word_list:
                for j in hot_list:
                    words = [word.strip('.,!_') for word in j.lower().split()]
                    if i in words:
                        wd[i] += words.count(i)

            srtd_hot = sorted(wd.items(), key=lambda v: (-v[1], v[0].lower()))
            for i in srtd_hot:
                if i[1] != 0:
                    print(f"{i[0]}: {i[1]}")
    except Exception:
        return
