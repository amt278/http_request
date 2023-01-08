import requests

url='https://httpbin.org'

params = {
    'name': 'adham',
    'age': 21
}

payload = {
    'data': 100    
}
headers = {
    'User-Agent': 'macOS',
    'Accept': 'image/jpeg'
}

response = requests.get(url+'/status/404')
#response = requests.get(url+'/get', params=params)
#response = requests.get(url+'/user-agent', headers=headers)
#response = requests.post(url+'/post', data=payload)
try:
    timeout_response = requests.get(url+'/delay/5', timeout=3)
except:
    print('timeout')

#image = requests.get(url+'/image', headers=headers)
#with open('image.jpg', 'wb') as f:
#    f.write(image.content)

print(f'status code: {response.status_code}')
if response.status_code == requests.codes.not_found:
    print('not found')

#response_dir = response.json()
#print(f'json: {response_dir}')

response_text = response.text
#print(f'response: {response_text}')
