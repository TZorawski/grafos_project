# -*- coding: utf-8 -*-
import sys
grafo = [[0]]


def add_node(label):
    grafo[0].append(label)
    n = [label]
    for i in range (len(grafo[0])-1):
        n.append(0)
    grafo.append(n)

    for node in grafo[1::]:
        node.append(0)
    
    print(grafo)

add_node('a1')
add_node('b1')
add_node('c1')
add_node('d1')