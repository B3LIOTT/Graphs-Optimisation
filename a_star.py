from graph import Graph
from math import sqrt, pow
import time
import heapq


class A_STAR:
    """
    Algorithme de recherche A*
    """

    def __init__(self, G: Graph):
        """
        :param G: graph
        """
        self.G = G
        self.start = G.s
        self.goal = G.t
        self.open_list = []
        self.cameFrom = {}
        self.path = []
        self.current = None
        self.cost = 0
        self.heuristic = 0
        self.start_time = None
        self.h_type = 1

    def h(self, node):
        """
        :param node: noeud actuel
        :return: cout entre le noeud node et l'arrivée t
        """
        if self.h_type == 0:
            return 0
        current = self.G.nodes[node].euclideanIndex
        goal = self.G.nodes[self.G.t].euclideanIndex
        return sqrt(pow(goal[0] - current[0], 2) + pow(goal[1] - current[1], 2))

    def g(self, node):
        """
        :param node: noeud actuel
        :return: cout entre le noeud node et le depart s (euclidien)
        """
        current = self.G.nodes[node].euclideanIndex
        start = self.G.nodes[self.G.s].euclideanIndex
        return sqrt(pow(start[0]-current[0], 2) + pow(start[1]-current[1], 2))

    def g_manhattan(self, node):
        """
        :param node: noeud actuel
        :return: cout entre le noeud node et le depart s (manhattan)
        """
        current = self.G.nodes[node].euclideanIndex
        start = self.G.nodes[self.G.s].euclideanIndex
        return abs(start[0]-current[0]) + abs(start[1]-current[1])

    def f(self, node):
        return self.g(node) + self.h(node)

    def reconstructPath(self, node):
        """
        :param node: noeud actuel
        :return: chemin le plus court
        """
        print("Execution time: ", time.perf_counter()-self.start_time)
        path = [node]
        while node in self.cameFrom.keys():
            node = self.cameFrom[node]
            path.append(node)

        return path

    def d(self, current, neighbor):
        neighbors = self.G.nodes[current].neighbors
        if neighbor in neighbors:
            return neighbors[neighbor]
        else:
            print(f"Erreur: {neighbor} n'est pas un voisin de {current}")
            return float("inf")

    def search(self):
        self.start_time = time.perf_counter()

        heapq.heappush(self.open_list, (self.h(self.start), self.start))

        g = {}
        for node in self.G.nodes:
            g[node.id] = float("inf")
        g[self.start] = 0

        f = {}
        for node in self.G.nodes:
            f[node.id] = float("inf")
        f[self.start] = self.h(self.start)

        while self.open_list:
            _, current = heapq.heappop(self.open_list)

            if current == self.goal:
                return self.reconstructPath(current)

            for neighbor in self.G.nodes[current].neighbors:
                tentative_gScore = g[current] + self.d(current, neighbor)
                if tentative_gScore < g[neighbor]:
                    self.cameFrom[neighbor] = current
                    g[neighbor] = tentative_gScore
                    f[neighbor] = tentative_gScore + self.h(neighbor)
                    heapq.heappush(self.open_list, (f[neighbor], neighbor))

        print("A*: FAILURE")
        return None
