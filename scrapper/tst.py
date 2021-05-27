#import os
#print(os.path.expanduser('~'))
#myd = {'name': 'danish', 'age': 30, 'city': 'new york'}
#import os
#EMAIL_ADD = os.environ.get('EMAIL_USER')
#EMAIL_PASS = os.environ.get('EMAIL_PASS')
#print(EMAIL_ADD)
from bs4 import BeautifulSoup
import requests
try:
    source = requests.get("https://www.google.com").text
except requests.exceptions.ConnectionError:
    print("ho")