import numpy as np
import pandas as pd

def get_number():
    '''
        Getting the number of subredits that the user likes
    '''
    while True:
        try:
            x = int(input("How many subredits do you like? Please enter a number:"))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    return x

def get_subreddits(x, df):
    '''
        Processing the subreddits

        Returning a list of ratings by subreddits
        (Kipping the consistency between the position of the elements in the list and trainning data columns)

        This is the list that we will use to predict

    '''
    d = {}
    n = x
    df.columns = map(str.lower, df.columns)
    columns = [e.lower() for e in df.columns]
    new_df = pd.DataFrame()
    while n>0:
        subreddit = input("Enter a subreddit:").lower()
        if subreddit in columns:
            keys = subreddit
            values = n/x
            d[keys] = values
            n -= 1
        else:
            print("Your subreddit it's not in our data, please enter the subreddit again.")
    new_df = df.append(d, ignore_index=True).fillna(0)
    return list(new_df.iloc[-1].values)










