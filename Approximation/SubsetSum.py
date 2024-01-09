def MergeSorted(A, B):
    """ Merge two ordered lists eliminating duplicates
    """
    merged_list = A + B
    merged_list = list(set(merged_list))
    merged_list.sort()
    return merged_list

def summing(L, x, t):
    ret_list = []
    for i in L:
        if i + x < t:
            ret_list.append(i+x)
    return ret_list

def trim(L, delta):
    greedy_choice = L[0]
    L_trimmed = [greedy_choice]
    for i in range(1, len(L)):
        if greedy_choice < L[i] / (1+delta):
            greedy_choice = L[i]
            L_trimmed.append(greedy_choice)
    return L_trimmed


def ApproxSubsetSum(S, t, epsilon):
    n = len(S)
    L = [[0]]
    for i in range(1, n+1):
        L.append(MergeSorted(L[i-1], summing(L[i-1], S[i-1], t)))
        L[i] = trim(L[i], (epsilon / (2*n)) )
    return max(L[n])
        

if __name__ == "__main__":
    S = [3, 1, 5, 9, 12]
    t = 8
    print(ApproxSubsetSum(S, t, 2))