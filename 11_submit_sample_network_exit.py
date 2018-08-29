import requests

api_key = 'asdf1234asdf1234asdf1234'

url = 'https://panacea.threatgrid.com/api/v2/samples'

file_name = 'file.exe'

parameters = {'api_key': api_key, 'network_exit': 'ny-ven'}

with open(file_name, 'rb') as sample:
	r = requests.post(url, files={'sample': sample}, params=parameters)

print(r.json())
