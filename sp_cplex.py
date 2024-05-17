from docplex.mp.model import Model
from graph import Graph


class SHORT_PATH_CPLEX:
    """
    Solveur CPLEX, problème du plus court chemin
    """

    def __init__(self, name: str, G: Graph):
        """
        :param name: nom du problème
        :param G: graph
        """
        self.G = G

        # Modèle
        self.model = Model(name=name)
        x_dict = self.model.binary_var_dict(G.edges, name="x")  # x in {0, 1}

        # Contraintes
        self.model.add_constraint(
            self.model.sum(x_dict[G.s, k] for k in G.nodes[G.s].neighbors.keys()) + self.model.sum(
                x_dict[k, G.s] for k in G.nodes[G.s].neighbors.keys()) == 1
        )

        self.model.add_constraint(
            self.model.sum(x_dict[G.t, k] for k in G.nodes[G.t].neighbors.keys()) + self.model.sum(
                x_dict[k, G.t] for k in G.nodes[G.t].neighbors.keys()) == 1
        )

        for k in range(len(G.nodes)):
            if k == G.s or k == G.t:
                continue
            self.model.add_constraint(
                self.model.sum(x_dict[i, k] for i in G.nodes[k].neighbors.keys()) - self.model.sum(
                    x_dict[k, j] for j in G.nodes[k].neighbors.keys()) == 0
            )

        # Fonction objective
        self.model.minimize(
            self.model.sum(
                (G.nodes[i].neighbors[j] * x_dict[i, j]) for (i, j) in G.edges
            )
        )

    def solve(self, logging=True):
        """
        :return: solution cplex, string du meilleur chemin, liste des noeuds du plus court chemin
        """
        self.model.solve(log_output=logging)
        x = self.model.solution
        try:
            list_res = []
            i = 0
            for k, v in x.as_dict().items():
                if k.name.split('_')[1] not in list_res:
                    list_res.append(k.name.split('_')[1])

                if k.name.split('_')[2] not in list_res:
                    list_res.append(k.name.split('_')[2])

            return x, list_res
        except AttributeError:
            print("No solution found")
            return None

    def print_information(self):
        self.model.print_information()

    def print_solution(self):
        self.model.print_solution()

