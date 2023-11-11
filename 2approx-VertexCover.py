import networkx as nx
import matplotlib.pyplot as plt
from random import sample

# 2-approximation algorithm for Minimum Vertex Cover
def ApproxVertexCover(G_original):
    V = []
    G = G_original.copy()
    
    while not nx.is_empty(G):
        # select randomly u and v
        edge = sample(list(G.edges()), 1)[0]
        u, v = edge[0], edge[1]

        # add both to the solution
        V.append(u)
        V.append(v)

        # remove all edges incident to u or v
        remove_list_u = [x for x in list(G.edges(u)) if x!= (u, v)]
        G.remove_edges_from(remove_list_u)
        remove_list_v = [x for x in list(G.edges(v)) if x!= (v, u)]
        G.remove_edges_from(remove_list_v)

        # be sure that u and v are no longer selected
        G.remove_node(u)
        G.remove_node(v)
    return V
        


def main():
    # generate a random graph
    G = nx.fast_gnp_random_graph(10, 0.4)

    cov = ApproxVertexCover(G)

    # color the nodes to see the output
    color_map = ['red' if node in cov else 'green' for node in G] 
    nx.draw_networkx(G, node_color = color_map)
    plt.show()
    


if __name__ == "__main__":
    main()