# -*- coding: utf-8 -*-
import sys
# import grafo.vertice
import json
import requests

class Aplicacao ():
    def __init__(self):
        self.nome = ""

def main ():
  # Exemplo REQUEST
  # response = requests.get("http://jsonplaceholder.typicode.com/comments")

  # REQUEST para github
  # response = requests.get(
  #    'https://api.github.com/search/repositories',
  #    params=b'q=requests+language:python',
  # )
  # print(response.json())

  # REQUEST para Marvel
  # { "apikey": chave pública da api,
  # "ts": timestamp,
  # "hash": md5(timestamp+chave privada+chave publica) }
  parametros = {
  "apikey": "2fd86138ee4056a8d6f596e7fda4d0e6",
  "ts": "04/07/201922:39",
  "hash": "5c6402e11e0fb933909e9057c87a0b94"
  }

  # Pega todos os personagens
  # response = requests.get("https://gateway.marvel.com:443/v1/public/characters?", params=parametros)
  # print(response.json())

  # Pega o personagem 
  response = requests.get("https://gateway.marvel.com:443/v1/public/characters/1017100?", params=parametros)

  # print(response.json().data.results[0].description)
  data = response.json()['data']
  results = data['results'][0]
  name = results['name']
  description = results['description']
  print(name)
  print(description)

main()