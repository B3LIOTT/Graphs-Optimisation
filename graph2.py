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
        self.edges_number = None
        self.node_number = None
        self.s = None
        self.t = None
        self.shortest_path = []

        try:
            with open(filename, 'r') as f:
                lines = f.readlines()

                self.nodes_number, self.edges_number = tuple(map(int, lines[0].split(" ")))

                for k in range(self.edges_number):
                    i, j, cost = tuple(map(int, lines[k+1].split(" ")))
                    self.add_edge(edge=(i, j))

        except ValueError:
            print("Invalid file format")
        except FileNotFoundError:
            print(f"File {filename} not found")

    def add_node(self, node: Node):
        self.nodes.append(node)

    def delete_node(self, node: Node):
        self.nodes.remove(node)

    def add_edge(self, edge: (int, int)):
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

