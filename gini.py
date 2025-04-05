import requests
import ctypes

def config_python_wrapper(libname, argtypes, restype):
    """
    Configura el wrapper de Python para la librería C."""
    libwrapper = ctypes.CDLL('./lib/'+libname+'.so') #TODO: CAMBIAR A LA RUTA CORRECTA
    libwrapper.factorial.argtypes = argtypes    #TODO: VERIFICAR QUE SEAN LOS TIPOS CORRECTOS
    libwrapper.factorial.restype = restype      #TODO: VERIFICAR QUE SEAN LOS TIPOS CORRECTOS

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

#libgini = config_python_wrapper('libgini', ctypes.c_float, ctypes.c_uint)
#gini_value = libgini.gini(gini_value)