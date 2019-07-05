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

  # REQUEST para Marvel
  parametros = {
  "apikey": "2fd86138ee4056a8d6f596e7fda4d0e6",
  "ts": "04/07/201922:39",
  "hash": "5c6402e11e0fb933909e9057c87a0b94"
  }
  response = requests.get("https://gateway.marvel.com:443/v1/public/characters?", params=parametros)
  print(response.json())

main()