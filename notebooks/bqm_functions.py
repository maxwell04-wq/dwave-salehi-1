"""
This file contains all the functions used in the notebooks 
under the Binary Quadratic Model section.

Prepared by AkashNarayanan B
"""
import networkx as nx
import matplotlib.pyplot as plt
from dimod import BinaryQuadraticModel

# Task 3

linear = {'x1': 3, 'x2': -1, 'x3': 10, 'x4': 7}
quadratic = {('x1', 'x2'): 2, ('x1', 'x3'): -5, ('x2', 'x3'): 3, ('x3', 'x4'): 11}
offset = 8
vartype = 'BINARY'


def graph_viz(G):
    nx.draw_networkx(G, with_labels=True, node_size=700, width=3, font_size=14, font_weight='bold', font_color="whitesmoke")
    plt.tight_layout()
    plt.axis("off")
    plt.show()


def maxcut_viz(G, cut_nodes):
    if isinstance(cut_nodes, dict):
        cut = set()
        for node, value in cut_nodes.items():
            if value == 1:
                cut.add(node)
    else:
        cut = cut_nodes
    
    S0 = [node for node in G.nodes if node in cut]
    S1 = [node for node in G.nodes if node not in cut]

    cut_edges = [(u, v) for u, v in G.edges if (u in S0 and v not in S0) or (u in S1 and v not in S1)]
    uncut_edges = [(u, v) for u, v in G.edges if (u in S0 and v in S0) or (u in S1 and v in S1)]

    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, nodelist=S0, node_color="tab:red", node_size=700)
    nx.draw_networkx_nodes(G, pos, nodelist=S1, node_color="tab:green", node_size=700)
    nx.draw_networkx_edges(G, pos, edgelist=cut_edges, style='dashed',edge_color="tab:blue", alpha=0.7, width=3)
    nx.draw_networkx_edges(G, pos, edgelist=uncut_edges, style='solid', width=3)
    nx.draw_networkx_labels(G, pos, font_size=14, font_weight='bold', font_color="whitesmoke")

    plt.tight_layout()
    plt.axis("off")
    plt.show()