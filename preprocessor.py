import pandas as pd


def preprocess(df, region_df):
# filtering for Summer Olympics
    df = df[df['Season'] == 'Summer']
# to merge with region_df
    df = df.merge(region_df, on='NOC', how='left')
# to remove duplicates
    df.drop_duplicates(inplace=True)
# To create new columns to show the number of Gold,Silver or Bronze medals individually
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df
