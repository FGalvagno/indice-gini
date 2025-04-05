import requests
import ctypes


country_code = 'ARG'
params = {
    'format': 'json',
    'date': '2011:2020',
}

api_url = 'https://api.worldbank.org/v2/en/country/'+country_code+'/indicator/SI.POV.GINI'

res = requests.get(api_url, params=params)

if res:
	print('Response OK')
else:
	print('Response Failed')
print(res.status_code)
print(res)
print(res.text)
