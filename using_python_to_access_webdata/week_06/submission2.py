import json
import urllib.parse
import urllib.request

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()

    print('Retrieved',len(data),'characters')

    info = json.loads(data.decode('utf-8'))
    print('Place id:',info['results'][0]['place_id'])
