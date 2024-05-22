from docplex.mp.model import Model
from graph2 import Graph2

class TS_CPLEX:
    """
    Solveur CPLEX, problème du voyageur
    """

    def __init__(self, name: str, G: Graph2):
        """
        :param name: nom du problème
        :param G: graph
        """
        self.G = G

        # Modèle
        self.model = Model(name=name)
        x_dict = self.model.binary_var_dict(G.edges, name="x")  # x in {0, 1}
        u_dict = self.model.continuous_var_dict([1, len(G.nodes)], name="u")  # u >= 2

        # Contraintes
        e = [k for k in range(len(G.nodes))]
        for j in range(len(G.nodes)):
            _e = e.copy()
            _e.remove(j)
            self.model.add_constraint(
                self.model.sum(x_dict[i, j] for i in _e) == 1
            )

        e = [k for k in range(len(G.nodes))]
        for i in range(len(G.nodes)):
            _e = e.copy()
            _e.remove(i)
            self.model.add_constraint(
                self.model.sum(x_dict[i, j] for j in _e) == 1
            )

        for i, j in range(1, len(G.nodes)):
            if i != j:
                self.model.add_constraint(
                    u_dict[i] - u_dict[j] + 1 <= (len(G.nodes) - 1) * (1 - x_dict[i, j])
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
