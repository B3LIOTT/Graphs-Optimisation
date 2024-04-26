from graph import Graph
from sp_cplex import SHORT_PATH_CPLEX as SPC
from a_star import A_STAR
import sys


def a_star_solve(G: Graph):
    a_star = A_STAR(G)
    return a_star.search()


def cplex_solve(G: Graph):
    spc = SPC(name='cplex', G=G)
    res = spc.solve()

    G.add_solution(res[1])
    save_res(filename, res)


def save_res(filename: str, res):
    try:
        with open(f'solutions/sol_{filename}.txt', 'w') as f:
            f.write(f'{res[0]}')
            f.write('------------------------------\n')
            f.write(res[1])
    except Exception as e:
        print('Error while saving solution: ', e)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python main.py <filename>")
        print("Info: the file should be in the 'graphes' directory.")
        sys.exit(1)

    filename = sys.argv[1]
    graph = Graph(f'graphes/{filename}')

    for node in graph.nodes:
        print(node)

    # Résolution du problème avec A*
    #print(a_star_solve(graph))

    # Résolution du problème avec CPLEX
    cplex_solve(graph)

    # Plot the graph with the solution
    graph.plot()
