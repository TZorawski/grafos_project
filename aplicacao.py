# -*- coding: utf-8 -*-
import sys
# import grafo.vertice
import json
import requests
import networkx as nx
# import matplotlib.pyplot as plt # import necessário para gerar um gráfico, import Fail

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
        if p.getName == nome:
            return p
        else:
            None

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

    # --------------------------------------------------------------------------------------------------------------------------
    # PEGA TODOS OS PERSONAGENS-------------------------------------------------------------------------------------------------
    # Limite = 100 personagens
    # response = requests.get("https://gateway.marvel.com:443/v1/public/characters?limit=101", params=parametros) # limit = 101+ não funciona
    response = requests.get("https://gateway.marvel.com:443/v1/public/characters?limit=10", params=parametros) #limit 100- funciona
    # print(response.json())

    # --------------------------------------------------------------------------------------------------------------------------
    # PEGA O PERSONAGEM --------------------------------------------------------------------------------------------------------
    # response = requests.get("https://gateway.marvel.com:443/v1/public/characters/1017100?", params=parametros)

    # # print(response.json().data.results[0].description)

    # print(response.json())
    data = response.json()['data']
    # results = data['results']

    G = nx.Graph() # adicionando um Grafo em networkX
    obj = []

    # --------------------------------------------------------------------------------------------------------------------------
    # ADICIONA OS DADOS DA API NO GRAFO -------------------------------------------------------------------------------------
    # PROBLEMA: não está aceitando o objeto completo, por enquanto está populando o grafo somente com o nome dos personagens.
    for v in data['results']:
        comics_add = []
        comics = v['comics']
        items = comics['items']
        for i in items:
            comics_add.append(i['name'])

        obj = Character(v['name'], v['description'], comics_add, v['stories'])
        G.add_node(obj) # adicionando um Nó em networkX
        comics_add = []
    # Printa os nós(nomes dos personagens) a partir do grafo
    for node in G:
        for node2 in G:
            if(node != node2):
                for comic in node.getComics():
                    if(comic in node.getComics()):
                        G.add_edge(node,node2)
                        # print("adiciona aresta entre: ", node.getName(), " e ", node2.getName(), " comic: ", comic)
        # print("----------------------- Comics ---------------------------")
        # Exemplo simples da composição dos Comics
        # {u'available': 0, u'items': [], u'returned': 0, u'collectionURI': u'http://gateway.marvel.com/v1/public/characters/1011266/stories'}
        # print(aux['collectionURI'])
        # print(aux['items'][0])
        # print()

    # --------------------------------------------------------------------------------------------------------------------------
    # QUEM FAZ COMICS COM QUEM ------------------------------------------------------------------------------------------------------
        # for node2 in G:
        #     for i in range(len(node.getStories()['items'])):
        #         for j in range(len(node2.getStories()['items'])):
        #             if (i != j)
        #             if((node.getStories()['items'][i] == node2.getStories()['items'][j]) and node.getStories()['items'][i] not in ):

        #                 G.add_edge(node, node2) # cria a aresta p/ conectar os dois nós
                        # print('-------------------------------------------------------------------------------------------------')
                        # print(node.getName())
                        # print(node.getStories()['items'][i])
                        # print('igual a:')
                        # print(node2.getName())
                        # print(node2.getStories()['items'][j])
                        # print('-------------------------------------------------------------------------------------------------')

    # --------------------------------------------------------------------------------------------------------------------------
    # EXECUTA A PROCURA DE DISTÂNCIA ------------------------------------------------------------------------------------------------------

    lista_personagens = list(G.nodes)
    for p in lista_personagens:
        print("Person: ", str(p.getName()))
    # print(lista_personagens[0].getName())
    # print(listac[0].getName())

    # for c in listac:
    #     print(c.getName())

    # while True:
    try:
        menor_caminho = nx.shortest_path(G, lista_personagens[0], lista_personagens[1])
        for c in menor_caminho:
            print(c.getName())

    except:
        print('Não foi possível encontrar um caminho entre os dois atores\n')


    # print('Vértices(Personagens): ')
    # print(G.number_of_nodes())
    # print('Arestas(co-working em um comic):')
    # print(G.number_of_edges())

    # shortest_path = nx.shortest_path(G, actor1, actor2)
    # print('Foi encontrado um caminho entre os dois atores!')
    # print('A distância mínima é ', len(shortest_path)-1)

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
