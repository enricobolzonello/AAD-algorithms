import ApproxVertexCover as vc

def BadApproxMaxClique(G):
    r""" Returns a bad approximation of a Max Clique.

    Uses the fact that any maximum clique $V^\prime$ in G is associated to a minimum vertex cover $V-V^\prime$ in $G^C$, and vice versa.

    The approximation ratio is,

    .. math::
        g_{AC} \ge \frac{|V|/2+1}{2}\approx \frac{|V|}{4}

    """
    V = vc.ApproxVertexCover(nx.complement(G))
    return list(set(G.nodes())-set(V))

def GreedyApproxMaxClique(G_original):
    r""" Returns a better approximation of a Max Clique.

    Uses a greedy approach.

    The approximation ratio is,

    .. math::
        g_{|V|} = \Omega(\log |V|)

    """
    V = []
    G = G_original.copy()
    
    while not nx.is_empty(G):
        # select the vertex with higher degree
        u = sorted(G.degree, key=lambda x: x[1], reverse=True)[0][0]

        # add to the solution
        V.append(u)

        # remove the node, this will remove also all edges
        G.remove_node(u)
    return V