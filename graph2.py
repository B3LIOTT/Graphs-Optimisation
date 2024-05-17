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
                    data = lines[k + 1].split(" ")
                    i, j = (int(data[0]), int(data[1]))
                    cost = float(data[2])
                    self.add_edge(edge=(i, j), cost=cost)

                for edge in self.edges:
                    i, j = edge[0]
                    if i not in [node.id for node in self.nodes]:
                        current_node = Node(name=f"{i}", id=i, euclideanIndex=(i, i), nodeType=None, neighbors={})
                        current_node.add_neighbor(neighbor=j, distance=edge[1])
                        self.add_node(current_node)

                    if j not in [node.id for node in self.nodes]:
                        current_node = Node(name=f"{j}", id=j, euclideanIndex=(j, j), nodeType=None, neighbors={})
                        current_node.add_neighbor(neighbor=i, distance=edge[1])
                        self.add_node(current_node)

        except ValueError:
            print("Invalid file format")
        except FileNotFoundError:
            print(f"File {filename} not found")

    def add_node(self, node: Node):
        self.nodes.append(node)

    def delete_node(self, node: Node):
        self.nodes.remove(node)

    def add_edge(self, edge: (int, int), cost: float):
        self.edges.append((edge, cost))

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

