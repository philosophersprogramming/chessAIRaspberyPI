import requests
from decode import *
url = "http://localhost:9081/gamestat"
key = decode()
payload = {'reset': 'true',
'iswhite': 'true'}
files=[

]
headers = {
  'authorization': 'Bearer ' + key
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
