# -*- coding: utf-8 -*-
import sys
# import grafo.vertice
import json
import requests
import networkx as nx

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

    # Pega todos os personagens -------------------------------------------------
    # Limite = 100 personagens
    response = requests.get("https://gateway.marvel.com:443/v1/public/characters?limit=10", params=parametros)
    # print(response.json())

    # Pega o personagem ---------------------------------------------------------
    # response = requests.get("https://gateway.marvel.com:443/v1/public/characters/1017100?", params=parametros)

    # # print(response.json().data.results[0].description)

    data = response.json()['data']
    # results = data['results']

    G = nx.Graph() # adicionando um Grafo em networkX
    obj = []
    # Adiciona os dados da API no Grafo -------------------------------------------------------------------------------------
    # PROBLEMA: não está aceitando o objeto completo, por enquanto está populando o grafo somente com o nome dos personagens.
    for v in data['results']:
        obj = Character(v['name'], v['description'], v['comics'], v['stories'])
        G.add_node(obj) # adicionando um Nó em networkX

    # Printa os nós(nomes dos personagens) a partir do grafo
    for node in G:
        print("----------------------- Comics ---------------------------")
        print(node.getComics())

main()

# ------------------------- Exemplos networkX -------------------------
# nx.test() # executa testes
# G = nx.Graph() # adicionando um Grafo em networkX
# G.add_node(1) # adicionando um Nó em networkX
# G.add_nodes_from([2, 3]) # adicionando uma lista de Nós
# # um nó pode ser composto por números, palavras, objetos, etc... indefinido.
#
# G.add_edge(1, 2) # adicionando uma aresta
# e = (2, 3) # aresta
# G.add_edge(*e) # adicionando uma aresta
#
# G.add_edges_from([(1, 2), (1, 3)]) #adicionando uma lista de arestas
#
# # G.clear() # remover todos os vértices e arestas.
#
# print(G.number_of_nodes()) # função que retorna o número de nós
# print(G.number_of_edges()) # função que retorna o número de arestas
#
# # remover vértices & arestas
# # G.remove_node()
# # G.remove_nodes_from()
# # G.remove_edge()
# # G.remove_edges_from()
#
# H = nx.DiGraph(G) # cria um dígrafo
#
# # acessando arestas e vizinhos
# G[1]  # same as G.adj[1]
# G[1][2]
#
# # caso a aresta ja exista podemos realizar atribuições a elas.
# G[1][3]['color'] = "blue"
# G.edges[1, 2]['color'] = "red"
#
# # adicionando atributos a arestas
# G.add_edge(1, 2, weight = 4.7 )
