import pandas as pd
from tqdm import tqdm
from datetime import datetime
from psycopg2 import connect
import numpy as np


def basic_checks(df):
    df['name'] = df['name'].str.replace("'","’",regex=True)
    df['host_name'] = df['host_name'].str.replace("'","’",regex=True)
    df['neighbourhood_group'] = df['neighbourhood_group'].str.replace("'","’",regex=True)
    df['neighbourhood'] = df['neighbourhood'].str.replace("'","’",regex=True)
    df['room_type'] = df['room_type'].str.replace("'","’",regex=True)

    # fill nan values
    df['reviews_per_month'].fillna(0,inplace = True)
    df['last_review'].fillna("1947-08-15",inplace=True)
    df['name'].fillna('',inplace = True)
    df['host_name'].fillna('',inplace = True)

    # Normalize the data
    df['review_date'] = pd.to_datetime(df['last_review']).dt.date
    df['review_time'] = pd.to_datetime(df['last_review']).dt.time

    # additional metrics
    avg_price_per_neighbourhood = df.groupby('neighbourhood')['price'].mean().reset_index()
    avg_price_per_neighbourhood.columns = ['neighbourhood', 'avg_price_per_neighbourhood']

    df = pd.merge(df,avg_price_per_neighbourhood,on='neighbourhood')

    return df