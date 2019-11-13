# encoding=utf-8

import codecs
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
import sys
import time
import requests
import os

def shindan(name):
    params = urllib.parse.urlencode({"u" : name})
    url = format("https://shindanmaker.com/870681")
    result = urllib.request.urlopen(url, data = params.encode('ascii'))
    soup = BeautifulSoup(result.read(), 'html.parser')
    content = soup.find('div', {'class' : 'result2'}).find('div')
    result_name = "".join(content.contents).strip()
    return result_name

file_name = sys.argv[1]
file_data = codecs.open(file_name, "r", "shift_jis")

def writeAllHanamachi():
    line = file_data.readline()
    while line:
        nameRemovedNewline = line.strip(os.linesep)
        result_name = shindan(nameRemovedNewline)
        print ("%s %s" % (line.strip(os.linesep), result_name))
        time.sleep(0.5)
        line = file_data.readline()

def writeJustHanamachi():
    flag = 0
    line = file_data.readline()
    while line:
        result_name = shindan(line)
        if result_name == "はなまちすみれ":
            print (line)
            flag = 1
        time.sleep(0.5)
        line = file_data.readline()
    return flag

mode = sys.argv[2]
if mode == "view":
    writeAllHanamachi()

if mode == "search":
    flag = writeJustHanamachi()
    if flag == 0:
        print ("はなまちすみれなかった")

file_data.close()
