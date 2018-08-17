import requests

api_key = 'a1b2c3d4e5f6g7h8i9j0k1l2m3'

url = 'https://panacea.threatgrid.com/api/v2/samples'

sample_url = 'https://www.cisco.com'

sample_template = '[InternetShortcut]\nURL={}'.format(sample_url)

sample = {'sample': sample_template}

parameters = {'api_key': api_key}

r = requests.post(url, files=sample, params=parameters)

print(r.json())
