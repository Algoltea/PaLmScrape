from FunctionFile import combine_files, remove_links_function, clean
import os
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

file_name = f'{config["Reddit"]["CLIENT_ID"]}'


directory = os.path.join(os.getcwd(), 'AddedDS')

if not os.path.exists(directory):
    os.makedirs(directory)

# Could this all be one function or just return one file? yes
# But incase one of the files breaks this allows me to trace it back
# You issue part 2
# AddedDS is a bad directory name, but I couldn't think of anything better
combine_files(f'{config["Reddit"]["SUBREDDIT"]}_data', f'{directory}/{config["Reddit"]["SUBREDDIT"]}_data_shrunk_2')
remove_links_function(f'{directory}/{config["Reddit"]["SUBREDDIT"]}_data_shrunk_2', f'{directory}/{config["Reddit"]["SUBREDDIT"]}_data_shrunk_3')
clean(f'{directory}/{config["Reddit"]["SUBREDDIT"]}_data_shrunk_3').to_csv(f'{directory}/{config["Reddit"]["SUBREDDIT"]}_data_shrunk_4.csv', index=False)