import requests

api_key = 'a1b2c3d4e5f6g7h8i9j0k1l2m3'

url = 'https://panacea.threatgrid.com/api/v2/samples'

file_name = 'file.exe'

parameters = {'api_key': api_key, 'vm':'win10'}

with open(file_name, 'rb') as sample:
	r = requests.post(url, files={'sample': sample}, params=parameters)

print(r.json())
