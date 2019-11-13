# encoding=utf-8

import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
import sys
import time
import requests


def shindan(name):
    params = urllib.parse.urlencode({"u" : name})
    url = format("https://shindanmaker.com/870681")
    result = urllib.request.urlopen(url, data = params.encode('ascii'))
    soup = BeautifulSoup(result.read(), 'html.parser')
    content = soup.find('div', {'class' : 'result2'}).find('div')
    print ("%s" % ('\n\t'.join(content.contents).strip()))


    
name = sys.argv[1]
# for num in sys.argv[2:]:
shindan(name)
time.sleep(0.1)
