import networkx as nx
import matplotlib.pyplot as plt
import random

def Christofides(G_original):
    r""" Returns an approximation of the solution of Triangle-TSP (Travelling Salesman Problem), which is a TSP (https://en.wikipedia.org/wiki/Travelling_salesman_problem) with the additional constraint that the distances form a metric space.
    This means that edge weights:
        - are symmetric
        - obey the triangular inequality

    The approximation ratio is,

    .. math::
        g_{AC} \le \frac{3}{2}

    """
    # find the minimum spanning tree
    T = nx.minimum_spanning_tree(G_original)

    # keep only the nodes with odd degree
    G_copy = G_original.copy()
    rmv_list = [n for n, d in T.degree if d%2 == 0]
    G_copy.remove_nodes_from(rmv_list)

    # min cost matching
    M = nx.min_weight_matching(G_copy)

    # declare the MultiGraph and combine edges
    MG = nx.MultiGraph()
    MG.add_edges_from(T.edges)
    MG.add_edges_from(M)

    # Euler tour
    W = nx.eulerian_circuit(MG)

    # shortcutting
    nodes = []
    for u, v in W:
        if not nodes:
            nodes.append(u)
        if u not in nodes:
            nodes.append(u)
    nodes.append(nodes[0])
    
    return nodes



def main():
    tsp = nx.approximation.traveling_salesman_problem

    G = nx.complete_graph(5)
    nx.set_edge_attributes(G, values = 1, name = 'weight')
    G[0][2]['weight'] = 2
    G[1][3]['weight'] = 2
    H = G.copy()

    cycle = Christofides(G)
    assert cycle == tsp(G)
    edge_list = list(nx.utils.pairwise(cycle))

    pos = nx.spring_layout(G)

    nx.draw_networkx(H, pos=pos, edge_color="blue", width=0.5)

    # Draw the route
    nx.draw_networkx_edges(
        H,
        pos=pos,
        edgelist=edge_list,
        edge_color="red",
        width=3,
    )

    print("The route of the salesman is:", cycle)
    plt.show()


if __name__ == "__main__":
    main()