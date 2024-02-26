import requests
from decode import *
url = "http://localhost:9081/upload"
key = decode()
payload = {}
files=[
  ('file',('test1.png',open('/Users/akash/Source/chessAI/chessboard/Testing/game 1/test1.png','rb'),'image/png'))
]
headers = {
  'authorization': 'Bearer ' + key
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
