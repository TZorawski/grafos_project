# -*- coding: utf-8 -*-
import sys

class Vertice ():
    def __init__(self, valor, rotulo):
        self.valor = valor
        self.rotulo = rotulo
        self.lista_adjacencia = []

    def get_lista_adjacencia(self):
        return self.lista_adjacencia