import requests

api_key = 'm9mc56i9l0qanaclufb3kc5jtn'

url = 'https://panacea.threatgrid.com/api/v3/session/whoami?api_key={}'.format(api_key)

r = requests.get(url)

print r.json()
