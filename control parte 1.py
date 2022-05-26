
import requests
import json

def show():
    response= requests.get('https://randomuser.me/api')
    consulta=json.loads(response.txt)
    if (consulta['results'][0]['gender']) == "female":
        print(consulta['results'][0]['name']['first'],consulta['results'][0]['name']['last'],consulta['results'][0]['location']['street']['name'],consulta['results'][0]['location']['street']['number'],consulta['results'][0]['location']['city'])
    else:
        print(consulta['results'][0]['name']['first'],consulta['results'][0]['name']['last'],consulta['results'][0]['login']['username'],consulta['results'][0]['login']['password'])