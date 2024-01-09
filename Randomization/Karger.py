import networkx as nx
import copy
import matplotlib.pyplot as plt
import math
import random

d = 30

def FullContraction(G):
    G_copy = copy.deepcopy(G)
    n = len(G_copy) - 2
    for i in range(n):
        # select a random edge
        chosen_edge = random.choice(list(G_copy.edges))
        # contract
        nx.contracted_nodes(G_copy, chosen_edge[0], chosen_edge[1])
    return len(G_copy.edges)

def Karger(G):
    min_cont = float('inf')
    n = len(G)
    s = math.floor(d * ((n**2)/2) * math.log(n)) # amplify to get the wrong result with probability < 1/n^d
    for _ in range(s):
	    t = FullContraction(G)
	    min_cont = min(min_cont, t)
    return min_cont

if __name__ == "__main__":
    G = nx.MultiGraph()
    G.add_edges_from([(1, 2), (1, 2), (1,4), (1,4), (1,3), (2,3), (2,5), (4,5), (4,5)])

    print(Karger(G))