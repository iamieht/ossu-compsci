import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter url: ')
    if len(address) < 1: break

    uh = urllib.request.urlopen(address, context=ctx)
    data = uh.read()

    print('Retrieved', len(data), 'characters')
    info = json.loads(data)
    #print(info)
    print('User count:', len(info['comments']))

    total = 0
    for item in info['comments']:
        total += item['count']
    
    print('Sum:', total)


# URLS
# http://py4e-data.dr-chuck.net/comments_42.json
# http://py4e-data.dr-chuck.net/comments_1179046.json