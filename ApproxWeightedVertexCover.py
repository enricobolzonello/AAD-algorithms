import networkx as nx
import matplotlib.pyplot as plt
from random import sample

r"""
Given a node-weighted undirected graph, determine a vertex cover $V^\prime \subseteq V$ minimizing

.. math::
    c(V^\prime) = \sum_{u\in V^\prime}w(u)

Note that letting $w(u)=1 \forall u\in V$ we obtain Minimum Vertex Cover
"""

def FairPricing(G_original):
    r""" Fair Pricing method for solving Approximate Weighted Vertex Cover

    Assumes that each node in the graph has an attribute named weight. 
    The approximation ratio is:
    .. math::
        g = \frac{C(V^\prime)}{C(V^*)} \le \frac{2C(V^*)}{C(V^*)} \le 2

    When $w(u)=1 \forall u\in V$ (unweighted case) the analysis becomes the one used for Approximate Vertex Cover

    """
    G = G_original.copy()

    while not nx.is_empty(G):
        edge = sample(list(G.edges()), 1)[0]
        u,v = edge[0], edge[1]

        w_u = G.nodes[u]["weight"]
        w_v = G.nodes[v]["weight"]

        p = min(w_u, w_v)

        G.nodes[u]["weight"] -= p
        G.nodes[v]["weight"] -= p

        G.remove_edge(u,v)

    return [node for node, weight in list(G.nodes(data="weight")) if weight == 0]

def main():
    G = nx.Graph()

    G.add_node(1, weight=3)
    G.add_node(2, weight=4)
    G.add_node(3, weight=5)
    G.add_node(4, weight=3)

    G.add_edge(1,2)
    G.add_edge(1,3)
    G.add_edge(2,3)
    G.add_edge(2,4)
    G.add_edge(3,4)

    cov = FairPricing(G)

    # color the nodes to see the output
    color_map = ['red' if node in cov else 'green' for node in G] 
    nx.draw_networkx(G, node_color = color_map)
    plt.show()
    

if __name__ == "__main__":
    main()