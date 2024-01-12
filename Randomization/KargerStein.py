import networkx as nx
import random
import copy
import math
from Karger import Karger

def PartialContraction(G, k):
    G_copy = copy.deepcopy(G)
    for i in range(k):
        # select a random edge
        chosen_edge = random.choice(list(G_copy.edges))
        # contract
        nx.contracted_nodes(G_copy, chosen_edge[0], chosen_edge[1], copy=False)
    return G_copy

def KargerStein(G):
    if len(G) <= 8: 
        return Karger(G)
    else:
        n = len(G)
        k = n - math.ceil(n/math.sqrt(n) + 1) # see analysis 
        G1 = PartialContraction(G,k)
        G2 = PartialContraction(G,k)
        return min(KargerStein(G1), KargerStein(G2))
    
if __name__ == "__main__":
    G = nx.MultiGraph()
    G.add_edges_from([(1, 2), (1, 2), (1,4), (1,4), (1,3), (2,3), (2,5), (4,5), (4,5), (5,6), (6,7), (7,3), (8,1), (8, 5), (9,0)])

    print(KargerStein(G))