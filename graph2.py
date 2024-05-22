import sys

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
        self.edges_number = None
        self.nodes_number = None
        self.shortest_path = []

        try:
            with open(filename, 'r') as f:
                lines = f.readlines()

                self.nodes_number, self.edges_number = tuple(map(int, lines[0].split(" ")))
                self.shape = (self.nodes_number, self.nodes_number)

                for k in range(self.edges_number):
                    data = lines[k + 1].split(" ")
                    i, j = (int(data[0]), int(data[1]))
                    cost = float(data[2])
                    self.add_edge(edge=(i, j, cost))

                nodes_dict = {}
                shape = self.nodes_number//(self.nodes_number**0.5)
                for edge in self.edges:
                    i, j = edge[0], edge[1]
                    if i not in nodes_dict:
                        current_node = Node(name=f"{i}", id=i, euclideanIndex=(i // shape, i % shape), nodeType=1, neighbors={})
                        current_node.add_neighbor(neighbor=j, distance=edge[2])
                        nodes_dict[i] = current_node
                    else:
                        nodes_dict[i].add_neighbor(neighbor=j, distance=edge[2])

                    if j not in nodes_dict:
                        current_node = Node(name=f"{j}", id=j, euclideanIndex=(j // shape, j % shape), nodeType=1, neighbors={})
                        current_node.add_neighbor(neighbor=i, distance=edge[2])
                        nodes_dict[j] = current_node
                    else:
                        nodes_dict[j].add_neighbor(neighbor=i, distance=edge[2])

                self.nodes = [Node(name=f"{k}", id=k, euclideanIndex=(k // shape, k % shape), nodeType=0, neighbors={}) for k in range(self.nodes_number)]
                for node in nodes_dict.values():
                    self.nodes[node.id] = node

        except ValueError:
            print("Invalid file format")
            sys.exit(1)
        except FileNotFoundError:
            print(f"File {filename} not found")
            sys.exit(1)

    def add_node(self, node: Node):
        self.nodes.append(node)

    def delete_node(self, node: Node):
        self.nodes.remove(node)

    def add_edge(self, edge: (int, int, float)):
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
        plotter.plot(self, algType=2)

