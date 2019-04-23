# -*- coding: utf-8 -*-
import sys
from vertice import Vertice
from aresta import Aresta

class Grafo ():
    def __init__(self, is_digrafo):
        self.lista_vertices = []
        self.lista_arestas = []
        self.matriz_adj = []
        self.is_digrafo = is_digrafo

    def add_vertice (self, vertice):
        self.lista_vertices.append(vertice)
        self.add_vertice_matriz_adj()   # adiciona novo vértice na matriz_adj
    
    def add_aresta (self, aresta):
        # a1 = Aresta(vertice1, vertice2, rotulo, valor)
        self.lista_arestas.append(aresta)
        self.add_conexao_matriz_adj(aresta)    # preenche matriz_adj

    def get_vertice (self, rotulo):
        for v in self.lista_vertices:
            if(v.rotulo == rotulo):
                return v

    def add_vertice_matriz_adj(self):
        # insere nova coluna para representar novo vertice
        for j in range (len(self.lista_vertices) - 1):
            self.matriz_adj[j].append(0)

        # insere nova linha para representar novo vertice
        nova_linha = []
        for i in range (len(self.lista_vertices)):
            nova_linha.append(0)
        self.matriz_adj.append(nova_linha)

    # liga vertices
    def add_conexao_matriz_adj(self, aresta):
        pos1 = self.encontra_pos_vertice(aresta.vertice1)
        pos2 = self.encontra_pos_vertice(aresta.vertice2)
        
        # se grafo é digrado, vertice1 vai para vertice2
        self.matriz_adj[pos1][pos2] = 1

        # se grafo não é digrado, vertice2 também vai para vertice1
        if (self.is_digrafo == False):
            self.matriz_adj[pos2][pos1] = 1
        

    # def get_aresta (self, rotulo):
    #     for v in self.lista_vertices:
    #         if(v.rotulo == rotulo):
    #             return v
    
    def get_ordem (self):
        return len(self.lista_vertices)

    # retorna grau do vértice
    # se for digrafo => [grau_entrada, grau_saida]
    # se não for digrafo => [grau_vertice, 0]
    def get_grau (self, vertice, is_grafo_digrafo):
        grau_entrada = 0
        grau_saida = 0
        pos = self.encontra_pos_vertice(vertice)
        
        for l in self.matriz_adj[pos]:
            if (l == 1):
                grau_saida += 1

        if (is_grafo_digrafo == True):
            for i in self.matriz_adj:
                if (i[pos] == 1):
                    grau_entrada += 1

        return [grau_saida, grau_entrada]

    # retorna lista de nós adjacentes
    def get_adjacentes (self, vertice):
        pos = self.encontra_pos_vertice(vertice)
        adjacentes = []

        if (pos >= 0):
            for i in range (len(self.matriz_adj[pos])):
                if (self.matriz_adj[pos][i] == 1):
                    adjacentes.append(self.lista_vertices[i])
        
        return adjacentes

    # retorna a posição do vértice
    # caso ele não pertença ao grafo, retorna -1
    def encontra_pos_vertice (self, vertice):
        for i in range (len(self.lista_vertices)):
            if vertice.rotulo == self.lista_vertices[i].rotulo:
                return i
        return -1

    def busca_largura (self, vertice):
        # cria estrutura adicional para gerenciar cores dos vertices na busca
        cores_vertices = [] # 0: branco; 1: cinza; 2: preto
        for i in range (len(self.lista_vertices)):
            cores_vertices.append(0)
    
    # busca_profundudade
    def dfs (self):
        # cria estrutura adicional para gerenciar cores dos vertices na busca
        cores_vertices = [] # 0: branco; 1: cinza; 2: preto
        for i in range (len(self.lista_vertices)):
            cores_vertices.append(0)
        
        # se é branco, visita
        for v in self.lista_vertices:
            pos = self.encontra_pos_vertice(v)
            if cores_vertices[pos] == 0:
                cores_vertices = self.dfs_visit(v, cores_vertices)

    def dfs_visit (self, vertice, cores_vertices):
        pos = self.encontra_pos_vertice(vertice)
        cores_vertices[pos] = 1 # vertice esta sendo visitado - fica cinza

        for i in range (len(self.lista_vertices)):
            if cores_vertices[i] == 0 and (i != pos):
                lista_v = self.lista_vertices
                cores_vertices = self.dfs_visit(lista_v[i], cores_vertices)
        cores_vertices[pos] = 2 # vertice foi visitado - fica preto
        return cores_vertices

    # imprime grafo
    def __repr__(self):
        return '(Nº vertices: {} É digrafo: {}\nMatriz adj: {})'.format(len(self.lista_vertices), self.is_digrafo, self.matriz_adj)

    def getFTD (self, v1):        
        pos = encontra_pos_vertice(v1)
        FTDlist.append(v1) # O PRÓPRIO VÉRTICE PERTENCE AO FTD
        aux = get_adjacentes(v1) 

        for i in range (len(aux)): # OS VÉRTICES ADJACENTES AO V1 PERTENCEM AO FTD
            FTDlist.append(aux[i])

        #Percorrer o FTD 
        #Inclui no FTD se o vértice não existe no FTD

        # for j in range (len(self.matriz_adj[pos])): #com base na qtde de vértices existentes
        #     if (self.matriz_adj[[pos][j]] == 1): # caso o valor na coluna correspondente ao 'i' seja 1:
        #         FTDlist.append(self.lista_vertices[j]) # incluo o vértice corresponednte ao indice 'i' no FTDlist
        