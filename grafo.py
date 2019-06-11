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
    def get_grau (self, vertice):
        grau_entrada = 0
        grau_saida = 0
        pos = self.encontra_pos_vertice(vertice)
        
        for l in self.matriz_adj[pos]:
            if (l == 1):
                grau_saida += 1

        if (self.is_digrafo == True):
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

    # retorna se grafo é completo
    def is_completo(self):
        for i in range(len(self.lista_vertices)):
            for j in range(0 if self.is_digrafo == True else i, len(self.lista_vertices)):
                if((i == j and self.matriz_adj[i][j] != 0) or (i != j and self.matriz_adj[i][j] != 1)):
                    return False
        
        return True
    
    # retorna se grafo é conexo
    def is_conexo(self, vertices_encontrados = None, vertice_inicial = None):
        if vertices_encontrados is None:
            vertices_encontrados = set()        # inicializa conjunto

        vertices = self.lista_vertices

        if not vertice_inicial:
            vertice_inicial = vertices[0]

        vertices_encontrados.add(vertice_inicial)

        if(len(vertices_encontrados) != len(vertices)):
            for vertice in self.get_adjacentes(vertice_inicial):
                if(vertice not in vertices_encontrados):
                    if(self.is_conexo(vertices_encontrados, vertice)):
                        return True
        else:
            return True
        return False

    # retorna se há ou não ciclo no grafo
    def is_ciclico(self, vertice = None, vertices_visitados = [], vertice_pai = None):
        if(vertice is None):
            vertice = self.lista_vertices[0]
        
        vertices_visitados.append(vertice)

        for adjacent in self.get_adjacentes(vertice):
            if(adjacent not in vertices_visitados):
                if(self.is_ciclico(adjacent, vertices_visitados, vertice)):
                    return True
            elif(adjacent != vertice_pai):
                return True
  
        return False

    # retorna se grafo é uma árvore
    def is_arvore(self):
        vertices_visitados = []

        if(self.is_ciclico(None, vertices_visitados)): 
            return False
        
        for vertice in self.lista_vertices: 
            if(vertice not in vertices_visitados): 
                return False
        
        return True

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

    #----------------------------------------------------------------------------------------

    # def existsInFtd(self, FTDlist, v):
    #     pos1 = self.encontra_pos_vertice(v)
    #     for i in range(len(FTDlist)):
    #         pos2 = self.encontra_pos_vertice(FTDlist[i])
    #         if(self.matriz_adj[pos1][pos2] == 1):
    #             flag = 0

    #     if(flag == 0):
    #         print(flag)
    #         return False # Se v já existe no FTD, não permite a inclusão novamente
    #     if(flag == 1):
    #         print(flag)
    #         return True # Se v não existe no FTD, manda incluir
        
    # def getFTD (self, v1):
    #     FTDlist = []
    #     FTDlist.append(v1) # O PRÓPRIO VÉRTICE PERTENCE AO FTD
    #     aux = self.get_adjacentes(v1)
    #     j = 1
    #     while(j < len(FTDlist)+1):
    #         for i in range (len(aux)): # OS VÉRTICES ADJACENTES A qualquer vértice na FTDlist PERTENCEM AO FTD
    #             if(self.existsInFtd(FTDlist, aux[i])): # Caso o vértice não exista no FTD, insere 
    # #                 FTDlist.append(aux[i])

    #         # for i in range (len(FTDlist)):
    #         #     print(len(FTDlist))

    #         if(FTDlist[j]):
    #             aux = self.get_adjacentes(FTDlist[j])
    #         j += 1
        
    #     print('FTDlist: ')
    #     for i in range (len(FTDlist)):
    #         print(FTDlist[i].rotulo)        
    
    #----------------------------------------------------------------------------------------

    # def ordenacao_topologica (self):
    #     grau_entrada = []
    #     fila = []
    #     for v in self.lista_vertices:
    #         grau_entrada.append(self.get_grau(v))
        
    #     for i in range (len(self.lista_vertices)):
    #         if grau_entrada[i] == 0:
    #         # fila.push() continuar