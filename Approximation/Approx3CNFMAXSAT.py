import random
import numpy as np

def bitnot(x):
    return 1-x

def checkclause(clause, assignment):
    result = 0
    for i in range(3):
            j = abs(clause[i])
            result = result or ((not assignment[j-1]) if np.sign(clause[i]) == -1 else assignment[j-1])
    return result


def Approx3CNFMAXSAT(clauses, variables):
    n = len(variables)
    m = len(clauses)

    b = [0] * n
    for i in range(n):
        b[i] = random.randint(0,1)

    print(b)
    
    Y = 0
    for j in range(m):
        if checkclause(clauses[j], b) == 1:
            Y += 1
    return Y


if __name__ == "__main__":
    clauses = [[1,-2,-3],[-1,2,-3],[-1,-2,3],[1,2,-3],[-1,2,3],[1,-2,3]] 
    variables = list(set([abs(l) for clause in clauses for l in clause])) 
    print(Approx3CNFMAXSAT(clauses, variables))