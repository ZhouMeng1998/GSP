from encodings import utf_8
import snscrape.modules.twitter as snstwitter
import pandas as pd
import html
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# query = "covid  (china OR lockdown) -new -year min_retweets:100 lang:en until:2021-11-13 since:2021-06-11 -filter:links -filter:replies"
query = "Covid lang:en until:2022-06-02 since:2021-04-04 -filter:links -filter:replies"
tweets = []
limit = 600

for tweet in snstwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
        break
    else:
        # tweets.append([tweet.date, tweet.user.username, tweet.content]
        tweets.append([tweet.content])

df = pd.DataFrame(tweets, columns=['Content'])
print(df)
# df.to_excel('elon_bitcoin.xlsx', sheet_name='sheet1', index=False)
df.to_csv('covid_tweets_600.csv', sep='\t', index=False)

# df.to_csv('covid_time.csv', index=False, sep='\t')
