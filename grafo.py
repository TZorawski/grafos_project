# -*- coding: utf-8 -*-
import sys
from vertice import Vertice
from aresta import Aresta

class Grafo ():
    def __init__(self, is_digrafo):
        self.lista_vertices = []
        self.lista_arestas = []
        # implementar matriz de adjacencia
        self.is_digrafo = is_digrafo

    def add_vertice (self, vertice):
        self.lista_vertices.append(vertice)
    
    def add_aresta (self, vertice1, vertice2, rotulo, valor):
        a1 = Aresta(vertice1, vertice2, rotulo, valor)
        self.lista_arestas.append(a1)

    def get_vertice (self, rotulo):
        for v in self.lista_vertices:
            if(v.rotulo == rotulo):
                return v

    # def get_aresta (self, rotulo):
    #     for v in self.lista_vertices:
    #         if(v.rotulo == rotulo):
    #             return v
    
    def get_ordem (self):
        return len(self.lista_vertices)

    #def get_grau (self, vertice):
        # implementar matriz de adjacencia primeiro

# def add_node(label):
# #     grafo = [[0]]
#     grafo[0].append(label)
#     n = [label]
#     for i in range (len(grafo[0])-1):
#         n.append(0)
#     grafo.append(n)

#     for node in grafo[1::]:
#         node.append(0)
    
#     print(grafo)

# add_node('a1')
# add_node('b1')
# add_node('c1')
# add_node('d1')