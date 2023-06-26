# PaLm Scrape

This is a GitHub repository for a Python project that scrapes data from Reddit using the PRAW library. 
The project allows you to specify a subreddit, a time period, and a number of posts to scrape. 
The scraped data includes the post title, score, body (if there is one) and comments. 
The data is stored in a CSV file for further analysis.

### Requirements

To run this project, you need to have Python 3 and the following libraries installed:

- PRAW ~=7.7.0
- Pandas ~=1.5.3

You also need to have a Reddit account and register an app on https://www.reddit.com/prefs/apps/ to get the Client ID and Client secret.

### Usage

To use this project, clone or download this repository and navigate to the folder where it is located. Then, open (or add to config_example.ini and remove the _example from the end leaving just config.ini) the config.ini file and enter your Reddit credentials and app information also modify the parameters according to your preferences. For example:
* LIMIT = 5
* TIME_FILTER = year

If you want to search by hot, new, or anything other than top, go to FindPosts.py and change "wanted_subreddit.top" to "wanted_subreddit.hot" or whatever you want to sort by.
#### Disclaimer
Run the files in the order of FindPosts.py -> ScrapePosts.py -> Main.py .

This should be fixed in the future but not at the moment. 

I should also add a forced rate limit of 50 a minute, but haven't yet.
*Supposedly PRAW actually has the rate limit built in*