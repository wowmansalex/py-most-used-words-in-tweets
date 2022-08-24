import os
import re
import json
from dotenv import load_dotenv
import datetime
import tweepy
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import FreqDist
import matplotlib.pyplot as plt
import numpy as np

load_dotenv()

bearer_token = os.environ.get("TWITTER_BEARER_TOKEN")

client = tweepy.Client(bearer_token)

query = input('pick a topic to see the most frequent used words\n')

response = client.search_recent_tweets(query, max_results=100)

with open('tweet.txt', 'w') as tweets:
  for tweet in response.data:
    tweets.write("%s\n" % tweet)
  print('done')

nltk.download('punkt')
nltk.download('stopwords')

stop_words = [ 'retweet', 'like', 'thanks', 'it', '\'', 'of', ')', '(', '.', '!', ',', '#', '?', ':', 'rt', 'https', '@', 'stop', 'the', 'to', 'and', 'a', 'in', 'it', 'is', 'I', 'that', 'had', 'on', 'for', 'were', 'was']
filtered_words = []
words = []
count = []

source = open('tweet.txt', 'r')

f = source.read()

string = f.lower()

cleaned_up = re.sub('[^A-Za-z0-9]+', '', string)

cleaned_up = word_tokenize(string)

for word in cleaned_up:
  if word not in stop_words:
    filtered_words.append(word)

freq = FreqDist(filtered_words)
most_common = freq.most_common(20)
for item in most_common:
  words.append(item[0])
  count.append(item[1])

plt.plot(words, count)
plt.ylabel('Word Count')
plt.xlabel('Words used the most')
plt.show()
