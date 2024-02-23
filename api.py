import requests
import json
from os import environ as env
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
AUDIENCE = env.get("AUDIENCE")
GRANT_TYPE = env.get("GRANT_TYPE")
CLIENT_SECRET = env.get("CLIENT_SECRET")
CLIENT_ID = env.get("CLIENT_ID")
url = env.get("URL")
payload = json.dumps({
  "client_id": CLIENT_ID,
  "client_secret": CLIENT_SECRET,
  "audience": AUDIENCE,
  "grant_type": GRANT_TYPE
})
headers = {
  'content-type': 'application/json',
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

