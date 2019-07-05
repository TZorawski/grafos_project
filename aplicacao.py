# -*- coding: utf-8 -*-
import sys
import grafo.vertice
import json
import requests

class Aplicacao ():
    def __init__(self):
        self.nome = ""

def main ():
  response = requests.get("http://jsonplaceholder.typicode.com/comments")
  # response = requests.get("http://gateway.marvel.com/v1/public/comics")
  print(response.json())

main()