#import urllib2
import requests
from collections import Counter
from bs4 import BeautifulSoup
import nltk, re, pprint
from nltk import word_tokenize

if __name__ == '__main__':
    url = "https://en.wikipedia.org/wiki/Bloodborne"
    print 'Reading: '+ url
    html_page = requests.get('https://en.wikipedia.org/wiki/Bloodborne')
    html_page.encoding = 'utf8'
    soup = BeautifulSoup(html_page.text,'html.parser')
    raw = soup.get_text()
    tokens = word_tokenize(raw)
    text = nltk.Text(tokens)
    print text.concordance('difficult')
    print text.concordance('difficulty')
