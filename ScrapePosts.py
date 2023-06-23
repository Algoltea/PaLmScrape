import os
import pandas as pd
import praw
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

reddit = praw.Reddit(client_id=config["Reddit"]["CLIENT_ID"],
                     client_secret=config["Reddit"]["CLIENT_SECRET"],
                     password=config["Reddit"]["PASSWORD"],
                     user_agent=config["Reddit"]["USER_AGENT"],
                     username=config["Reddit"]["USERNAME"])

posts = pd.read_csv(f'{config["Reddit"]["SUBREDDIT"]}.csv')

os.mkdir(f'{config["Reddit"]["SUBREDDIT"]}_data')

for i in range(len(posts)):
    print(f'working on post... {posts.iloc[i,2]}')
    comment_body = []
    submission = reddit.submission(id=f'{posts.iloc[i,2]}')
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        print(f'working... {comment}')
        if isinstance(comment.parent(), praw.models.Comment):
            parent = comment.parent()
            parent_body = parent.body
        else:
            parent_body = comment.submission.title
        if parent_body != "[removed]" and comment.body != "[removed]" and parent_body != "[deleted]" and comment.body != "[deleted]":
            comment_body.append([comment.id, comment.body, parent_body, posts.iloc[i, 2]])
    comment_body = pd.DataFrame(comment_body, columns=['id', 'body', 'parent', 'post'])
    comment_body.to_csv(f'{config["Reddit"]["SUBREDDIT"]}_data/{config["Reddit"]["SUBREDDIT"]}-body-{posts.iloc[i, 2]}.csv', index=False)