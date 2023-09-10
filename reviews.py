import pandas as pd

reviews = pd.read_csv("data/winemag-data-130k-v2.csv.zip")


df = reviews.groupby('country').agg({'country':'count', 'points':'mean'}).round(1)
dfupdated = df.rename(columns = {'country': 'count'})
dfupdated = dfupdated.sort_values('count', ascending=False) 

#print(dfupdated)
df.to_csv('data/reviews-per-country.csv')

