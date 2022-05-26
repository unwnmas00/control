import requests
import json

def comment(n):
    response= requests.get('https://jsonplaceholder.typicode.com/comments')
    consulta = json.loads(response.text)
    holo = {'comentario' : consulta[n]['body']}
    return holo

print(comment(10))