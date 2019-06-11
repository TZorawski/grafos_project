# -*- coding: utf-8 -*-
import sys
from grafo import Grafo
from vertice import Vertice
from aresta import Aresta

def main():

    g1 = Grafo(False) # gera um grafo sem direção
    v1 = Vertice("a", 12) # cria o vérice v1
    g1.add_vertice(v1) # insere o vérice v1 no grafo g1

    v2 = Vertice("b", 13) # cria o vértice v2
    g1.add_vertice(v2) # insere o vértice v2 no grafo g1

    v3 = Vertice("c", 6) # cria o vértice v3
    g1.add_vertice(v3) # insere o cértice v3 no grafo v3

    a1 = Aresta(v1, v2, "a1", 2) # cria uma aresta entre v1 e v2
    a2 = Aresta(v2, v3, "a2", 2) # cria uma aresta entre v2 e v3
    a3 = Aresta(v3, v1, "a3", 2) # cria uma aresta entre v3 e v1

    # corrigir
    g1.add_aresta(a1) # insere a aresta a1 no grafo
    g1.add_aresta(a2) # insere a aresta a2 no grafo
    g1.add_aresta(a3) # insere a aresta a3 no grafo
    
    print(g1)

    g1.dfs()

main()