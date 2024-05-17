from node import Node
from math import sqrt


class Graph2:
    """
    Classe représentant un graphe (dans ce TP on considère des graphes non orientés)
    """

    def __init__(self, filename: str):
        """
        :param filename: nom du fichier contenant la description du graphe
        :param graphType: type du graphe (1: graphe pour l'exercice 1, 2: graphe pour l'exercice 2)
        """
        self.nodes = []
        self.edges = []
        self.shape = ()
        self.s = None
        self.t = None
        self.salesman_travel = []

        try:
            with open(filename, 'r') as f:
                lines = f.readlines()

                try:
                    # get the shape of the graph in the first line
                    self.shape = tuple(map(int, lines[0].split(" ")))

                    # get the values
                    vals = [[int(val) for val in line.strip().split(" ")] for line in lines[1:]]

                except ValueError:
                    print("Invalid file format")

                # create the nodes
                for i in range(self.shape[0]):
                    for j in range(self.shape[1]):
                        if vals[i][j] == 2:
                            self.s = i*self.shape[1]+j
                        if vals[i][j] == 3:
                            self.t = i*self.shape[1]+j

                        node = Node(name=f"{i * self.shape[1] + j}", id=i * self.shape[1] + j, euclideanIndex=(i, j), nodeType=vals[i][j],
                                    neighbors={})

                        if vals[i][j] != 0:
                            # get neighbors
                            directions = [
                                (-1, 0, 1), (1, 0, 1), (0, -1, 1), (0, 1, 1),
                                (-1, -1, sqrt(2)), (-1, 1, sqrt(2)), (1, -1, sqrt(2)), (1, 1, sqrt(2))
                            ]
                            for di, dj, distance in directions:
                                ni, nj = i + di, j + dj
                                if 0 <= ni < self.shape[0] and 0 <= nj < self.shape[1] and vals[ni][nj] != 0:
                                    neighbor_id = ni * self.shape[1] + nj
                                    node.add_neighbor(neighbor=neighbor_id, distance=distance)
                                    self.edge(edge=(neighbor_id, node.id))

                        self.nodes.append(node)

        except FileNotFoundError:
            print(f"File {filename} not found")

    def add_node(self, node: Node):
        self.nodes.append(node)

    def delete_node(self, node: Node):
        self.nodes.remove(node)

    def edge(self, edge: (int, int)):
        self.edges.append(edge)

    def delete_egde(self, edge: (int, int)):
        self.edges.remove(edge)

    def add_solution(self, path: [int]):
        self.shortest_path = path

    def plot(self):
        """
        Plot the graph
        """
        import plotter
        plotter.plot(self)

