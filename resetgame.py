import requests

url = "http://localhost:9081/gamestat"

payload = {'reset': 'true'}
files=[

]
headers = {
  'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjdSTGY0MGY2dUVMX1FtVnJ1X3J5bCJ9.eyJpc3MiOiJodHRwczovL2Rldi13Z2VhdDJmcGtyZTNndGo0LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJVM3RHSjZDQUNGeTR5MUZFRTN3c0hkeGJiMHE1M3RYaEBjbGllbnRzIiwiYXVkIjoiaHR0cHM6Ly9jaGVzc2FpLmFrYXNoa2FsbHVta2FsLmNvbSIsImlhdCI6MTcwODI5NDU0NiwiZXhwIjoxNzA4MzgwOTQ2LCJhenAiOiJVM3RHSjZDQUNGeTR5MUZFRTN3c0hkeGJiMHE1M3RYaCIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyJ9.qPieqU78d7y8H7-2VSWfHSZm7jyGM96CVkAzTJ7IhpveOY8ZseDVSs0wjSCLGAj52EaoYCE_9mufl5H356d1KX30oKtmbKtXRtWQBmEwwb0GO4Qvr8pZv8ptZZFGhgpLLsZwyiAhGCY8fwQY0qoNdDKu1J0LnyyP_RuqQxw6ZB0wMgdj4JEXN8xWKhOnc0KpqZbqHTmpRBqp8sgId4zfLXgIwaGK55e4WUktxaEowg1CrctbVMAzPRTH4YTqxLLkIOQjStYqydjDcVGNiez__Qu_28henw4cxCtzJCR5i_BT_o4ZuBfvgtAJHO5JG9E6ad5hL0621HoVM3eCBfch2Q'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)