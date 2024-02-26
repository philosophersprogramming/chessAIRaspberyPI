import requests
from decode import *
from webcam import *
url = "http://localhost:9081/upload"
key = decode()
payload = {}
photo_stream = capture_as_stream()
files= {'file': ('photo.jpg', photo_stream, 'image/jpeg')}
headers = {
  'authorization': 'Bearer ' + key
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
