import requests

api_key = 'asdf1234asdf1234asdf1234'

url = 'https://panacea.threatgrid.com/api/v2/samples'

sample_url = 'https://www.cisco.com'

parameters = {'api_key': api_key,
              'url': sample_url}

r = requests.post(url, params=parameters)

print(r.json())
