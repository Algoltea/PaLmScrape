import pandas as pd
import re
import csv
import os
import glob


def c_len(x):
    f = pd.read_csv(x)
    return len(f)


def clean(x):
    df = pd.read_csv(f'{x}.csv')
    df.dropna(inplace=True)
    df.rename(columns={df.columns[0]: "completion", df.columns[1]: "prompt"}, inplace=True)
    return df


def combine_files(data, combined):
    os.chdir(f'{data}')
    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    # combine all files in the list
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
    combined_csv.drop(combined_csv.columns[[0, 3]], axis=1, inplace=True)
    combined_csv.dropna(inplace=True)
    # export to csv
    combined_csv.to_csv(f'{combined}.csv', index=False, encoding='utf-8')


def remove_links_function(read, write):
    with open(f'{read}.csv', "r",
              encoding="utf-8") as read_file:
        # create a csv reader object
        reader = csv.reader(read_file)
        # open a new file for writing
        with open(f'{write}.csv', "w", encoding="utf-8", newline='') as write_file:
            # create a csv writer object
            writer = csv.writer(write_file)
            # shrunk_2.csv
            for row in reader:
                # create an empty list to store the cleaned row
                clean_row = []
                # loop through each column in the row
                for col in row:
                    # remove any URLs from the column using regex
                    # can add .strip() to the end, not sure what it does tho in this case tbh, maybe its cool
                    # probably not
                    clean_col = re.sub(r'http\S+', '', col)
                    # append the cleaned column to the clean_row list
                    clean_row.append(clean_col)
                # write the clean_row list to shrunk_3.csv file
                writer.writerow(clean_row)