from graph import Graph
from graph2 import Graph2
from sp_cplex import SHORT_PATH_CPLEX as SPC
from a_star import A_STAR
import sys


def a_star_solve(G: Graph):
    a_star = A_STAR(G)
    res = a_star.search()
    if res is None:
        print("No solution found")
        return
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
    if len(sys.argv) != 4:
        print("Usage: python main.py <exercice> <alg type> <filename>")
        print("Exercices: 1=Shortest path, 2=Traveling salesman")
        print("Alg types: 1=CPLEX, 2=A*")
        print("Info: the file should be in the 'graphes' directory for Shortest path, or in 'graphes2' for Traveling salesman.")
        sys.exit(1)

    filename = sys.argv[3]

    if int(sys.argv[1]) == 1:
        graph = Graph(f'graphes/{filename}')
    elif int(sys.argv[1]) == 2:
        graph = Graph2(f'graphes2/{filename}')
    else:
        print("Exercice unknown (1 or 2)")
        sys.exit(1)

    for node in graph.nodes:
        print(node)

    algType = int(sys.argv[2])

    if algType == 1:
        # Résolution du problème avec CPLEX
        cplex_solve(graph)

    elif algType == 2:
        # Résolution du problème avec A*
        a_star_solve(graph)

    else:
        print("Invalid algorithm type (1 or 2)")
        sys.exit(1)

    # Plot the graph with the solution
    graph.plot()
