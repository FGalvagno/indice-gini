import requests
import ctypes
from msl.loadlib import Client64

class conversion(Client64):
    """Call a function in 'my_lib.dll' via the 'MyServer' wrapper."""

    def __init__(self):
        # Specify the name of the Python module to execute on the 32-bit server (i.e., 'my_server')
        super(conversion, self).__init__(module32='conversion.py')
    
    def convert_and_increment(self,n):
        # The Client64 class has a 'request32' method to send a request to the 32-bit server
        return self.request32('convert_and_increment', n)

country_code = 'ARG'
params = {
    'format': 'json',
    'date': '2022:2022',
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

print("Coeficiente de Gini ", res.json()[1][0]['value']) #TODO: CAMBIAR; solo funciona cuando tenemos un solo año
gini_value = res.json()[1][0]['value']


lib=conversion()
print(lib.convert_and_increment(44.7))
# Creamos nuestra función factorial en Python
# hace de Wrapper para llamar a la función de C
#def convertir(num):
#    return libconversion.converted_and_increment(num)  

#print(convertir(gini_value))
