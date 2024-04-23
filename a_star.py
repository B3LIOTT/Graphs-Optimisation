from graph import Graph


class A_STAR:
    """
    Algorithme de recherche A*
    """

    def __init__(self, G: Graph):
        """
        :param G: graph
        """
        self.G = G
        self.open_list = []
        self.closed_list = []
        self.path = []
        self.start = None
        self.goal = None
        self.current = None
        self.cost = 0
        self.heuristic = 0

    def set_start(self, start):
        self.start = start

    def set_goal(self, goal):
        self.goal = goal

    def get_neighbors(self):
        return self.G.edges[self.current]

    def get_cost(self, neighbor):
        return self.G.edges[self.current][neighbor]

    def get_heuristic(self, neighbor):
        return self.G.edges[neighbor][self.goal]

    def get_total_cost(self, neighbor):
        return self.get_cost(neighbor) + self.get_heuristic(neighbor)

    def get_path(self):
        return self.path

    def search(self):
        self.open_list.append(self.start)

        while self.open_list:
            self.current = self.open_list[0]

            for neighbor in self.get_neighbors():
                if neighbor not in self.closed_list:
                    if neighbor not in self.open_list:
                        self.open_list.append(neighbor)

            self.open_list.remove(self.current)
            self.closed_list.append(self.current)

            if self.current == self.goal:
                break

        self.path = self.closed_list

