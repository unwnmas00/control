from os import listxattr
import requests
import json


def georeference(n):
    response= requests.get('https://jsonplaceholder.typicode.com/users')
    consulta = json.loads(response.text)

    lista=[]
    
    lista.append(consulta[n]['name'])
    lista.append(consulta[n]['address']['geo']['lat'])
    lista.append(consulta[n]['address']['geo']['lng'])

    return lista

print(georeference(1))