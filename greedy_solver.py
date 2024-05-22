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

    def solve(self):
        """
        Solve the problem
        """
        # all permutations of the nodes
        path = []
        for node in self.graph.nodes:
            if node.nodeType == 1:
                path.append(node.id)

        start = path[0]
        perms = list(itertools.permutations(path[1:], len(path)-1))
        perms = [[start] + list(perm) for perm in perms]

        for perm in perms:
            cost = 0
            prev = perm[0]
            best_path = [prev]
            for node in perm[1:]:

                if node in self.graph.nodes[prev].neighbors:
                    cost += self.graph.nodes[prev].neighbors[node]
                    prev = node
                    best_path.append(node)
                else:
                    cost = float('inf')
                    break

            if cost < self.best_cost:
                self.best_cost = cost
                self.best_path = best_path


        if len(self.best_path) == 1:
            raise ValueError("No solution found")

        return [str(node) for node in self.best_path]
