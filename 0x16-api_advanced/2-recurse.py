#!/usr/bin/python3

import praw

reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                     client_secret='YOUR_CLIENT_SECRET',
                     user_agent='YOUR_USER_AGENT')


def recurse(subreddit, hot_list=None):
    if hot_list is None:
        hot_list = []

    try:
        subreddit = reddit.subreddit(subreddit)
        hot_articles = subreddit.hot(limit=None)

        for article in hot_articles:
            hot_list.append(article.title)

        if len(hot_list) == 0:
            return None

        if hot_articles.params.get('after'):
            return recurse(subreddit, hot_list)
        else:
            return hot_list

    except praw.exceptions.Redirect:
        return None
