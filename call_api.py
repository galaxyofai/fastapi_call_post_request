import requests

# url = 'http://localhost:8005/text'
url = 'http://127.0.0.1:8005/text'


headers = {'accept': 'application/json'}
data = {'msg_text': 'Welcome to the galaxy of ai'}

response = requests.post(url, headers=headers, params=data)

print(response.status_code)
print(response.json())
