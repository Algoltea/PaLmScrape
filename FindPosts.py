import praw
import pandas as pd
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

limit = int(config["Reddit"]["LIMIT"])
time_filter = str(config["Reddit"]["TIME_FILTER"])

reddit = praw.Reddit(client_id=config["Reddit"]["CLIENT_ID"],
                     client_secret=config["Reddit"]["CLIENT_SECRET"],
                     password=config["Reddit"]["PASSWORD"],
                     user_agent=config["Reddit"]["USER_AGENT"],
                     username=config["Reddit"]["USERNAME"])
# If you don't use password but remove the section of "password=config["Reddit"]["PASSWORD"],"

posts = []
wanted_subreddit = reddit.subreddit(config["Reddit"]["SUBREDDIT"])
# limit was moved to its own redundant variable because it was easier than searching for the line each time
# you problem if you dislike it tbh
for post in wanted_subreddit.top(time_filter=time_filter, limit=limit):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
posts = pd.DataFrame(posts, columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
print(posts)  # you should probably comment this out if I didn't already, It's just to test I didn't destroy everything
posts.to_csv(f'{config["Reddit"]["SUBREDDIT"]}.csv', index=False)
