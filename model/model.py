import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.Graph()
        self._idMap = {}
        self._idMapNome = {}
        self.dict = {}
        self._solBest = []
        self.allIngredienti=DAO.getAll()
        for v in self.allIngredienti:
            self._idMap[v.condiment_code] = v
        for v in self.allIngredienti:
            self._idMapNome[v.display_name] = v
        self._costBest = 0


    def creaGrafo(self, calorie):
        self.nodi = DAO.getNodi(calorie)
        self.grafo.add_nodes_from(DAO.getNodi(calorie))
        self.addEdges()
        self.analisimetodo()
        return self.grafo

    def addEdges(self):
         self.grafo.clear_edges()
         allEdges = DAO.getConnessioni()
         for connessione in allEdges:
             nodo1 = self._idMap[connessione.v1]
             nodo2 = self._idMap[connessione.v2]
             if nodo1 in self.grafo.nodes and nodo2 in self.grafo.nodes:
                 if self.grafo.has_edge(nodo1, nodo2) == False:
                     self.grafo.add_edge(nodo1, nodo2, weight=connessione.peso)

    def getNumNodes(self):
        return len(self.grafo.nodes)

    def getNumEdges(self):
        return len(self.grafo.edges)

    def analisimetodo(self):
        analisi=[]
        for cibo in self.grafo.nodes:
            analisi.append((cibo.display_name, cibo.condiment_calories, DAO.getNcibi(cibo.condiment_code)))
        analisiOrdinata=sorted(analisi, key=lambda x:x[1], reverse=True)
        return analisiOrdinata

    def getBestPath(self,v0Nome):
        v0=self._idMapNome[v0Nome]
        self._solBest = []
        self._costBest = 0
        parziale = []
        for v in self.grafo.nodes:
            parziale.append(v)
            self.ricorsione(parziale,v0)
            parziale.pop()
        return self._solBest, self._costBest

    def ricorsione(self, parziale,v0):
        # Controllo se parziale è una sol valida, ed in caso se è migliore del best
         if v0 in parziale:
            if self.peso(parziale) > self._costBest:
                self._costBest = self.peso(parziale)
                self._solBest = copy.deepcopy(parziale)

         for v in self.grafo.nodes:
             if v not in self.grafo.neighbors(parziale[-1]):
                if v not in parziale:
                    parziale.append(v)
                    self.ricorsione(parziale,v0)
                    parziale.pop()

    def peso(self,parziale):
        peso=0
        for nodi in parziale:
            peso+=nodi.condiment_calories
        return peso




