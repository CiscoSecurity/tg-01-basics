import requests

api_key = 'asdf1234asdf1234asdf1234'

q = 'cisco.com'

url = 'https://panacea.threatgrid.com/api/v2/search/submissions?q={}&api_key={}'.format(q, api_key)

r = requests.get(url)

print(r.json())
