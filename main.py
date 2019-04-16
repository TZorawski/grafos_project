# -*- coding: utf-8 -*-
import sys
from grafo import Grafo
from vertice import Vertice
from aresta import Aresta

def main():
    print("Heloo")

    g1 = Grafo(False)
    v1 = Vertice("a", 12)
    g1.add_vertice(v1)

    v2 = Vertice("b", 13)
    g1.add_vertice(v2)

    v3 = Vertice("c", 6)
    g1.add_vertice(v3)

    a1 = Aresta(v1, v2, "a1", 2)
    a2 = Aresta(v2, v3, "a2", 2)
    a3 = Aresta(v3, v1, "a3", 2)

    # corrigir
    # g1.add_aresta(a1)
    # g1.add_aresta(a2)
    # g1.add_aresta(a3)
    
    print(g1)

main()