from node import Node
from math import sqrt


class Graph:
    """
    Classe représentant un graphe (dans ce TP on considère des graphes non orientés)
    """

    def __init__(self, filename: str):
        """
        :param filename: nom du fichier contenant la description du graphe
        """
        self.nodes = []
        self.edges = []
        self.shape = ()
        self.s = None
        self.t = None
        self.shortest_path = []

        try:
            with open(filename, 'r') as f:
                lines = f.readlines()

                try:
                    # get the shape of the graph in the first line
                    self.shape = tuple(map(int, lines[0].split(" ")))
                    if self.shape[0] > 500 or self.shape[1] > 500:
                        raise ValueError("The size of the graph is too big")

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
                            if i > 0 and vals[i - 1][j] != 0:
                                node.add_neighbor(neighbor=(i - 1) * self.shape[1] + j, distance=1)
                                self.add_egde(((i - 1) * self.shape[1] + j, i * self.shape[1] + j))

                            if i < self.shape[0] - 1 and vals[i + 1][j] != 0:
                                node.add_neighbor(neighbor=(i + 1) * self.shape[1] + j, distance=1)
                                self.add_egde(((i + 1) * self.shape[1] + j, i * self.shape[1] + j))

                            if j > 0 and vals[i][j - 1] != 0:
                                node.add_neighbor(neighbor=i * self.shape[1] + j - 1, distance=1)
                                self.add_egde((i * self.shape[1] + j - 1, i * self.shape[1] + j))

                            if j < self.shape[1] - 1 and vals[i][j + 1] != 0:
                                node.add_neighbor(neighbor=i * self.shape[1] + j + 1, distance=1)
                                self.add_egde((i * self.shape[1] + j + 1, i * self.shape[1] + j))

                            if i > 0 and j > 0 and vals[i - 1][j - 1] != 0:
                                node.add_neighbor(neighbor=(i - 1) * self.shape[1] + j - 1, distance=sqrt(2))
                                self.add_egde(((i - 1) * self.shape[1] + j - 1, i * self.shape[1] + j))

                            if i > 0 and j < self.shape[1] - 1 and vals[i - 1][j + 1] != 0:
                                node.add_neighbor(neighbor=(i - 1) * self.shape[1] + j + 1, distance=sqrt(2))
                                self.add_egde(((i - 1) * self.shape[1] + j + 1, i * self.shape[1] + j))

                            if i < self.shape[0] - 1 and j > 0 and vals[i + 1][j - 1] != 0:
                                node.add_neighbor(neighbor=(i + 1) * self.shape[1] + j - 1, distance=sqrt(2))
                                self.add_egde(((i + 1) * self.shape[1] + j - 1, i * self.shape[1] + j))

                            if i < self.shape[0] - 1 and j < self.shape[1] - 1 and vals[i + 1][j + 1] != 0:
                                node.add_neighbor(neighbor=(i + 1) * self.shape[1] + j + 1, distance=sqrt(2))
                                self.add_egde(((i + 1) * self.shape[1] + j + 1, i * self.shape[1] + j))

                        self.nodes.append(node)

        except FileNotFoundError:
            print(f"File {filename} not found")

    def add_node(self, node: Node):
        self.nodes.append(node)

    def delete_node(self, node: Node):
        self.nodes.remove(node)

    def add_egde(self, edge: (int, int)):
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

