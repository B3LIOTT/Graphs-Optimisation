class Node:
    def __init__(self, name: str, id: int, euclideanIndex: (int, int), nodeType: int, neighbors: dict):
        """
        :param name: nom du noeud
        :param nodeType: type du noeud (0: obstacle, 1: traversable, 2: depart, 3: arrivee)
        :param neighbors: voisins du noeud (indice des noeuds voisins dans la liste des noeuds du graphe, distance)
        """
        self.name = name
        self.id = id
        self.euclideanIndex = euclideanIndex
        self.nodeType = nodeType
        self.neighbors = neighbors

    def get_dist_to_neighbor(self, neighbor: int):
        return self.neighbors[neighbor]

    def add_neighbor(self, neighbor: int, distance: float):
        self.neighbors[neighbor] = distance

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return f"Node {self.name} | Type {self.nodeType} | neighbors: {self.neighbors}"
