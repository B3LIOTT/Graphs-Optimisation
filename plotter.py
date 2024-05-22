import networkx as nx
import matplotlib.pyplot as plt
from graph import Graph
from constants import *
import sys


def plotFromFile(filename: str, algType: int):
    graph = Graph(f'graphes/{filename}')
    sol = []
    # recuperation de la solution
    try:
        if algType == 1:
            with open(f'solutions/sol_cplex_{filename}', 'r') as f:
                sol = f.read().split('\n')[0:-1]

        elif algType == 2:
            with open(f'solutions/sol_a-star_{filename}', 'r') as f:
                sol = f.read().split('\n')[0:-1]

        else:
            print("Type d'algorithme non valide (soit 1, soit 2)")
            return
    except FileNotFoundError:
        print("No solution found")
        return

    # ajout de la solution au graphe
    graph.add_solution(sol)

    # plot
    plot(graph, algType)


def plot(G: Graph, algType: int):
    # Create a graph
    nxG = nx.Graph()

    # Add nodes with coordinates
    for node in G.nodes:
        nxG.add_node(node.name, pos=(node.euclideanIndex[1], -node.euclideanIndex[0]))

    # Add edges between nodes
    for edge in G.edges:
        nxG.add_edge(str(edge[0]), str(edge[1]))

    # Add color to nodes which are in the shortest path
    colors = []
    for node in nxG.nodes:
        if node in G.shortest_path:
            if G.nodes[int(node)].nodeType == 2:
                colors.append(START)
            elif G.nodes[int(node)].nodeType == 3:
                colors.append(GOAL)
            else:
                colors.append(SP)
        elif G.nodes[int(node)].nodeType == 0:
            colors.append(OBSTACLE)
        else:
            colors.append(EMPTY)

    # Draw the graph with node coordinates
    pos = nx.get_node_attributes(nxG, 'pos')
    if algType == 1:
        nx.draw(nxG, pos, with_labels=False, node_size=100000/(G.shape[0]*G.shape[1]), node_color=colors)
    else:
        nx.draw(nxG, with_labels=False, node_size=100000 / (G.shape[0] * G.shape[1]), node_color=colors)

    # Show the plot
    plt.show()


def plotToCompare(G: Graph, sol1: [str], sol2: [str]):
    # Create a graph
    nxG = nx.Graph()

    # Add nodes with coordinates
    for node in G.nodes:
        nxG.add_node(node.name, pos=(node.euclideanIndex[1], -node.euclideanIndex[0]))

    # Add edges between nodes
    for edge in G.edges:
        nxG.add_edge(str(edge[0]), str(edge[1]))

    # Add color to nodes which are in the shortest path
    colors = []
    for node in nxG.nodes:
        if node in sol1:
            colors.append(START)
        elif node in sol2:
            colors.append(GOAL)

        elif G.nodes[int(node)].nodeType == 0:
            colors.append(OBSTACLE)
        else:
            colors.append(EMPTY)

    # Draw the graph with node coordinates
    pos = nx.get_node_attributes(nxG, 'pos')
    nx.draw(nxG, pos, with_labels=False, node_size=100000/(G.shape[0]*G.shape[1]), node_color=colors)

    # Show the plot
    plt.show()


def compareResults(filename):
    graph = Graph(f'graphes/{filename}')
    sol1 = []
    sol2 = []
    # recuperation de la solution
    try:
        with open(f'solutions/sol_cplex_{filename}', 'r') as f:
            sol1 = f.read().split('\n')[0:-1]

        with open(f'solutions/sol_a-star_{filename}', 'r') as f:
            sol2 = f.read().split('\n')[0:-1]

    except FileNotFoundError:
        print("No solution found")
        return

    # plot
    plotToCompare(graph, sol1, sol2)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python plotter.py <filename>")
        print("Info: the file should be in the 'graphes' directory.")
        sys.exit(1)

    algType = input("Pour afficher un résultat, enter the algorithm type (1=CPLEX, 2=A*).\nSinon entrez 0 pour comparer les résultats: ")

    filename = sys.argv[1]

    if at := int(algType) != 0:
        plotFromFile(filename, at)

    else:
        compareResults(filename)
