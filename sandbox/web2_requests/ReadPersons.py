import requests

url = "http://localhost:8085/web2/secure/face/firserver/ReadPersons"

payload="{ \"server_id\": \"1\", \"id\": [ ], \"page\": 1, \"pageSize\": 2 }"
headers = {
  'Content-Type': 'application/json',
  'Cookie': 'JSESSIONID=17a266a6-aedd-4f3f-b082-10ed2618c828'
}

response = requests.request("POST", url, headers=headers, data=payload, auth=('user', 'pass'))

print(response.text)