from graph2 import Graph2
import itertools


class GreedySolver:
    """
    Brute froce the Traveling Salesman problem
    """

    def __init__(self, graph: Graph2):
        self.graph = graph
        self.best_path = []
        self.best_cost = float('inf')
        self.visited = [False] * len(graph.nodes)

    def solve(self):
        """
        Solve the problem
        """
        # all permutations of the nodes
        path = [i for i in range(self.graph.nodes_number)]
        perms = list(itertools.permutations(path, self.graph.nodes_number))
        for perm in perms:
            cost = 0
            prev = perm[0]
            path = []
            for node in perm[1:]:
                path.append(prev)
                if node in self.graph.nodes[prev].neighbors:
                    cost += self.graph.nodes[prev].neighbors[node]
                    prev = node
                else:
                    cost = float('inf')
                    break
            if cost < self.best_cost:
                self.best_cost = cost
                self.best_path = path
