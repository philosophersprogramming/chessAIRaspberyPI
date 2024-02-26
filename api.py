import requests
import json
from os import environ as env
from dotenv import load_dotenv, find_dotenv
from cryptography.fernet import Fernet

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

if response.status_code == 200:
    token_data = response.json()
    access_token = token_data.get('access_token')

    # Load the encryption key from file
    with open('encryption_key.key', 'rb') as key_file:
        key = key_file.read()

    cipher_suite = Fernet(key)
    encrypted_token = cipher_suite.encrypt(access_token.encode())

    # Save the encrypted token to a file
    with open('oauth_token.pickle', 'wb') as f:
        f.write(encrypted_token)
    print("Encrypted OAuth token saved successfully.")
else:
    print("Failed to obtain OAuth token:", response.text)
