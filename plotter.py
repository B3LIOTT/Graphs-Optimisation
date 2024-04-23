import networkx as nx
import matplotlib.pyplot as plt
from graph import Graph
from constants import *


def plot(G: Graph):
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
            colors.append(SP)
        elif G.nodes[int(node)].nodeType == 0:
            colors.append(OBSTACLE)
        else:
            colors.append(EMPTY)

    # Draw the graph with node coordinates
    pos = nx.get_node_attributes(nxG, 'pos')
    nx.draw(nxG, pos, with_labels=False, node_size=100000/(G.shape[0]*G.shape[1]), node_color=colors)

    # Show the plot
    plt.show()
