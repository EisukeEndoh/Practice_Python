# encoding=utf-8

import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
import sys

def shindan(name, url):
    params = urllib.parse.urlencode({"u" : name})
    result = urllib.request.urlopen(url, data = params.encode('ascii'))
    soup = BeautifulSoup(result.read(), 'html.parser')
    content = soup.find('div', {'class' : 'result2'}).find('div')
    result_name = "".join(map(str,content.contents)).strip()
    print("%s" % (result_name))

name = sys.argv[1]
url = sys.argv[2]
shindan(name, url)
