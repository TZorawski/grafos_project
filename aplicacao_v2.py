# -*- coding: utf-8 -*-
import sys

import requests
import networkx as nx
import json

class Character():
    def __init__(self, name, description, comics, stories):
        self.__name = name
        self.__description = description
        self.__comics = comics
        self.__stories = stories

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setDescription(self, description):
        self.__description = description

    def getDescription(self):
        return self.__description

    def setComics(self, comics):
        self.__comics = comics

    def getComics(self):
        return self.__comics

    def setStories(self, stories):
        self.__stories = stories

    def getStories(self):
        return self.__stories


def getNodeByName (lista_personagens, nome) :
    for p in lista_personagens:
        if p.getName() == nome:
            return p
        else:
            None
    novo_nome = input("Nome inválido. Digite outro: ")
    return getNodeByName(lista_personagens, novo_nome)

def main ():
    parametros = {
    "apikey": "2fd86138ee4056a8d6f596e7fda4d0e6",
    "ts": "04/07/201922:39",
    "hash": "5c6402e11e0fb933909e9057c87a0b94"
    }
    
    G = nx.Graph()

    for i in range (14):
        response = requests.get("https://gateway.marvel.com:443/v1/public/characters?limit=100&offset=" + str(100*i), params=parametros) #limit 100- funciona
        data = response.json()['data']

        obj = []

        # Adiciona os vértices (Character) no grafo
        for v in data['results']:
            comics_add = []
            comics = v['comics']
            items = comics['items']
            for i in items:
                comics_add.append(i['name'])

            obj = Character(v['name'], v['description'], comics_add, v['stories'])
            G.add_node(obj)
            comics_add = []

        # Adiciona as arestas no grafo
        for node in G:
            for node2 in G:
                if(node != node2):
                    for comic in node.getComics():
                        if(comic in node2.getComics()):
                            G.add_edge(node,node2)


    lista_personagens = list(G.nodes)

    print("LISTA DE PERSONAGENS")
    for personagem in lista_personagens:
        print(personagem.getName())

    while True:
        node1 = input("Personagem 1: ")
        node1 = getNodeByName(lista_personagens, node1)
        # print(node1.getComics())

        node2 = input("Personagem 2: ")
        node2 = getNodeByName(lista_personagens, node2)
        # print(node2.getComics())

        menor_caminho = []
        try:
            menor_caminho = nx.shortest_path(G, node1, node2)
            
            if(len(menor_caminho) == 2): # Significa que não tem nenhum vértice entre os dois personagens
                print("Menor Caminho = 0")
                print("Esses personagens já participaram de um mesmo quadrinho")
            else: # Significa que tem um ou mais vértices entre os personagens
                for x in menor_caminho:
                    print(x.getName())
                print("Menor Caminho = ", len(menor_caminho) - 2)
        except:
            print('Não foi possível encontrar um caminho entre os dois atores\n')





main()