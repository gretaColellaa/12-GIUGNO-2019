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
            self._idMap[f.food_id] = f

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

