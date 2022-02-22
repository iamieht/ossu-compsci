# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = input('Enter count ')
pos = int(input('Enter position '))
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
count = int(count)
while count > 0:
    for tag in tags[pos-1:pos]:
        page = tag.get('href', None)
        print(page)
        html = urllib.request.urlopen(page, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
    count -= 1
