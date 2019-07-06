import os
import json

try:
	import requests

except:
	try:
		os.system('pip3 install requests')
	except:
		os.system('pip install requests')

if os.name == 'nt':
	os.system('cls')
else:
	os.system('clear')

id = str(input('Digite o ip a ser rastreado: '))


req = requests.get(f'https://ipapi.co/{id}/json/')
saida = json.loads(req.text)

print()
print(f'IP:     {saida["ip"]}')
print(f'País:   {saida["country"]}')
print(f'Estado: {saida["region"]}')
print(f'Cidade: {saida["city"]}')
print(f'Time:   {saida["timezone"]}')
print(f'Moeda:  {saida["currency"]}')
print(f'Lat:    {saida["latitude"]}')
print(f'Long:   {saida["longitude"]}')