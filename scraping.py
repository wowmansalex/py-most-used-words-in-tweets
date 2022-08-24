import os
import re
import json
from dotenv import load_dotenv
import datetime
import tweepy
import requests
from bs4 import BeautifulSoup

load_dotenv()

query = input("What do you want to search for?\n")

prices_mediamarkt = []
prices_phone_house = []
cheapest_mediamarkt = 0 
cheapest_phone_house = 0
prices_all = []

def mediamarkt(query):
  response = requests.request("GET", 'https://www.mediamarkt.es/es/search.html?query='+query+'&filter=category%3ACAT_ES_MM_262')
  soup = BeautifulSoup(response.text, 'html.parser')
  prices = soup.find_all('span', 'ScreenreaderTextSpan-sc-11hj9ix-0 kZCfsu') 
  articles = soup.find_all('p', 'BaseTypo-sc-1jga2g7-0 izkVco StyledInfoTypo-sc-1jga2g7-1 doYUxh')
  for article in articles:
    for price in prices:
      global prices_mediamarkt
      prices_mediamarkt.append('mm')
      prices_mediamarkt.append(article.text)
      prices_mediamarkt.append(float(price.text))
      
  # prices_mediamarkt.sort()
  print(prices_mediamarkt)
  # global cheapest_mediamarkt
  # cheapest_mediamarkt = prices_mediamarkt[0]

def phone_house(query): 
  response = requests.request("GET", 'https://www.phonehouse.es/?buscar-texto='+query+'&subcategoria=Smartphones')
  soup = BeautifulSoup(response.text, 'html.parser')
  
  prices = soup.find_all('span', 'precio precio-2') 
  
  for price in prices:
    clean = price.text.replace('€','').replace(',','.')
    global prices_phone_house
    prices_phone_house.append(float(clean))
  prices_phone_house.sort()
  global cheapest_phone_house
  cheapest_phone_house = prices_phone_house[0]
    
def get_prices():
  mediamarkt(query)
  phone_house(query)
  print(cheapest_mediamarkt, cheapest_phone_house)

get_prices()