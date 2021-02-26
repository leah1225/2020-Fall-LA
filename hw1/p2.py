from scipy.sparse import *
import numpy as np


def p2_has_cycle(sets):
    # TODO
    # return True if the graph has cycle; return False if not

    sets = csr_matrix(sets)

    current = 0
    mostTimes = sets.shape[0]*sets.shape[1]
    CycleExist = False
    original = sets.copy()

    while CycleExist == False:
        
        if current > mostTimes:
            break
            
        sets = csr_matrix(original).dot(csr_matrix(sets))
        
        # if there exists value >= 1 in the diagonal -> cycle found
        if (csr_matrix.diagonal(sets)>=1).any():
            CycleExist = True
            break
        
        current += 1
        
    if CycleExist == True:
          return True
    else:
          return False

