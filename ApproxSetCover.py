import copy

def findMaxSubset(U, I):
    max_len = 0
    max_subset = []
    for T in I:
        subset = set(U) & set(T)
        if len(subset) > max_len:
            max_len = len(subset)
            max_subset = subset
    return max_subset

def ApproxSetCover(X, I):
    U = copy.deepcopy(X)
    C = []
    while U:
        S = findMaxSubset(U, I)
        U = [e for e in U if e not in S]
        C.append(S)
    return C

if __name__ == "__main__":
    universe = set(range(1, 6))
    subsets = [[1,3],[2],[1,2,5],[3,5],[4],[5],[1,3],[2,4,5],[1,2],[2,3]]
    print(f"exp. 1: {ApproxSetCover(universe, subsets)}")

    universe2 = set(range(1,16))
    subsets2 = [[2, 7, 8, 10, 12, 13], [1, 3, 5, 8, 10, 11, 12, 15], [1, 2, 3, 4, 5, 6, 7, 12, 13], [2, 6, 7, 11, 12, 13], [9, 10, 12, 13], [1, 3, 7, 9, 11, 12, 13], [1, 3, 5, 6, 8, 9, 10, 11, 12, 13], [1, 3, 4, 5, 6, 7, 12, 14, 15], [1, 2, 3, 6, 11, 12], [1, 2, 4, 5, 7, 8], [5, 9, 10, 11, 15], [3, 5, 6, 7, 8, 9, 12, 13, 14], [1, 3, 4, 5, 6, 7, 9, 11, 13, 14, 15], [1, 3, 5, 6, 8, 12, 14], [2, 4, 7, 9, 10, 12, 14], [1, 3, 5, 6, 11, 15], [2, 3, 4, 5, 6, 8, 10, 11, 12, 13, 14, 15], [1, 2, 4, 6, 7, 11, 13, 14, 15], [1, 2, 8, 12, 13, 14], [1, 2, 6, 7, 8, 13], [1, 2, 3, 5, 7, 8, 10, 12, 14, 15], [4, 5, 7, 12, 15], [1, 2, 3, 5, 11, 14], [1, 6, 8, 11, 13], [1, 6, 7, 8, 9, 10, 13], [1, 2, 3, 4, 5, 9, 11, 15], [2, 3, 4, 7, 9, 11, 12], [1, 3, 4, 5, 8, 10, 11, 12, 13], [2, 8, 9, 10], [6, 11, 13], [2, 5, 6, 8, 9, 11, 12, 13, 15], [2, 4, 6, 7, 8, 9, 10, 11, 13, 15], [1, 2, 3, 4, 5, 7, 8, 10, 11], [1, 2, 6, 9, 11, 13, 14, 15], [1, 4, 9, 10, 11, 13, 15], [1, 2, 3, 4, 6, 8, 12, 14, 15], [4, 5, 7, 8, 10, 13, 14], [2, 4, 8, 9, 11, 14], [2, 3, 4, 5, 6, 7, 10, 11, 14], [1, 2, 4, 5, 6, 7, 9, 11, 13, 14, 15], [1, 2, 6, 7, 9, 10, 12, 15], [1, 3, 6, 9, 10, 15], [2, 3, 5, 7, 8, 9, 11], [2, 3, 4, 5, 8, 10, 11, 12, 15], [1, 3, 4, 5, 6, 7, 9, 10, 12, 15]]
    print(f"exp. 2: {ApproxSetCover(universe2, subsets2)}")
