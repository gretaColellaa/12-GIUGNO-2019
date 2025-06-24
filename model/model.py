import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._idMap = {}
        self._edges = []
        self._nodes = []
        self._grafo = nx.Graph()


    def crea_grafo(self, calorie):
        self._food = DAO.getNodes(calorie)

        for f in self._food:
            self._nodes.append(f.food_id)
            self._idMap[str(f)] = f

        self._edges = DAO.getEdges(calorie)
        self._grafo.add_nodes_from(self._nodes)
        self._grafo.add_edges_from(self._edges)
        # for u,v in self._grafo.edges:
        #     print(self._grafo.get_edge_data(u,v)['weight'])


    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)


    def getFood(self):
        return self._food

    def getFoodData(self, food):
        somma = 0
        if self._grafo.neighbors(food.food_id):
            for n in self._grafo.neighbors(food.food_id):
                somma += self._grafo.get_edge_data(food.food_id, n)['weight']
        return somma


    def getBestPath(self,v0Nome):
        v0=self._idMap[v0Nome]
        self._solBest = []
        self._costBest = 0
        parziale = []
        for v in self._grafo.nodes:
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

         for v in self._grafo.nodes:
             if v not in self._grafo.neighbors(parziale[-1]):
                if v not in parziale:
                    parziale.append(v)
                    self.ricorsione(parziale,v0)
                    parziale.pop()

    def peso(self,parziale):
        peso=0
        for nodi in parziale:
            peso+=nodi.calories
        return peso

