# -*- coding: utf-8 -*-
import sys
from vertice import Vertice

class Aresta ():
    def __init__(self, vertice1, vertice2, rotulo, valor):
        self.vertice1 = vertice1
        self.vertice2 = vertice2
        self.rotulo = rotulo
        self.valor = valor