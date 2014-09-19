import requests
url = 'http://hub.orisi.org/'

payload = {

            "source": "1",
            "destination": "1",
            "channel": "1",
            "signature": "1",
            "body": "",


}


data = {}

### Create file and open
import json
with open('test.json', 'w') as outfile:
  json.dump(data, outfile)

files = {'file': open('test.json', 'rb')}
r = requests.post(url, files=files, data=payload)
print r.text


