from graph import Graph
from sp_cplex import SHORT_PATH_CPLEX as SPC
from a_star import A_STAR
import sys


def a_star_solve(G: Graph):
    a_star = A_STAR(G)
    res = a_star.search()
    res_str = [str(n) for n in res]
    G.add_solution(res_str)
    save_res(f"a-star_{filename}", res_str)


def cplex_solve(G: Graph):
    spc = SPC(name='cplex', G=G)
    res = spc.solve()
    G.add_solution(res[1])
    save_res(f"cplex_{filename}", res[1])


def save_res(filename: str, res):
    try:
        with open(f'solutions/sol_{filename}', 'w') as f:
            for r in res:
                f.write(f'{r}\n')

    except Exception as e:
        print('Error while saving solution: ', e)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python main.py <alg type> <filename>")
        print("Alg types: 1=CPLEX, 2=A*")
        print("Info: the file should be in the 'graphes' directory.")
        sys.exit(1)

    filename = sys.argv[2]
    graph = Graph(f'graphes/{filename}')

    for node in graph.nodes:
        print(node)

    algType = int(sys.argv[1])

    if algType == 1:
        # Résolution du problème avec CPLEX
        cplex_solve(graph)

    elif algType == 2:
        # Résolution du problème avec A*
        a_star_solve(graph)

    else:
        print("Type d'algorithme non valide (soit 1, soit 2)")
        sys.exit(1)

    # Plot the graph with the solution
    graph.plot()
