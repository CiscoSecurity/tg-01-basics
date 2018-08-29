import requests

api_key = 'asdf1234asdf1234asdf1234'

url = 'https://panacea.threatgrid.com/api/v2/samples'

sample_url = 'https://www.cisco.com'

sample_template = '[InternetShortcut]\nURL={}'.format(sample_url)

sample = {'sample': sample_template}

parameters = {'api_key': api_key}

r = requests.post(url, files=sample, params=parameters)

print(r.json())
