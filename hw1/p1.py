from scipy.sparse import *
import numpy as np


def p1_has_cycle(sets):
    # TODO
    # return True if the graph has cycle; return False if not
    sets = csr_matrix(sets)
    
    elementNum = sets.shape[1] #  total number of elements in a row
    currentRow = 0
    totalRows = sets.shape[0] # total number of rows in the original graph
    CycleExist = False

    while CycleExist == False:
        
        if currentRow >= totalRows: # do row addition only once for each row in the graoh
              break

        rows = sets.shape[0]
        matrix1 = np.identity(rows-1) # identity matrix(rows-1*rows-1)
        vector1= np.ones(rows-1) #  vector with all 1s(rows-1*1)
        
        matrix1 = np.column_stack((vector1, matrix1))
        rowAdd = csr_matrix(matrix1).dot(csr_matrix(sets))

        #  checking each addition row
        for i in range(rowAdd.shape[0]): 
            num1 = np.sum(rowAdd.getrow(i)==1)
            num2 = np.sum(rowAdd.getrow(i)==-1)
            
            if np.sum(rowAdd.getrow(i)==0) == elementNum:
                CycleExist = True
                break
                
            elif(num1 == 1)and(num2 == 1):
                index1 = find(sets.getrow(0)==-1)[1][0]
                index2 = find(rowAdd.getrow(i)==-1)[1][0]
                
                if index1 == index2:
                    sets = vstack((sets, rowAdd[i]))
                    
        sets = sets[1:]
        currentRow += 1    

    if CycleExist == True:
          return True
    else:
          return False

