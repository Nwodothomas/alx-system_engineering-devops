#!/usr/bin/python3
"""
Queries the Reddit API recursively and returns a list containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively retrieves the titles of all hot articles for a given subreddit and stores them in a list.
    If the subreddit is invalid or no results are found, returns None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        children = data.get('children', [])
        after = data.get('after')

        for post in children:
            title = post.get('data', {}).get('title')
            if title:
                hot_list.append(title)

        if after:
            recurse(subreddit, hot_list, after=after)
        else:
            return hot_list
    else:
        return None
