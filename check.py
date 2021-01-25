import numpy as np

#table = np.array([[0, 0, 1],
#                 [1, 1, 0],
#                  [1, 1, 0]])
#print(table) 

def check_if_solved(a):
    # check rows
    if [1,1,1] in a.tolist(): 
        return 1
    elif [0,0,0] in a.tolist(): 
        return 0  
    # check columns
    for i in range(3): 
        res = 0
        for x in a[0:3, i:i+1]:
            if x == 1:
                res += x
            if res == 3:
                print('column ', i, ' is filled')
                return 1
        res = 3
        for x in a[0:3, i:i+1]:
            if x == 0:
                res -= 1
            if res == 0:
                print('column ', i, ' is filled')
                return 0
    # check diagonal, main
    for x in range(2):
        if a[0,0] == a[1,1] == a[2,2] == x:
            return x
    # check diagonal, side
    for x in range(2):
        if a[2,0] == a[1,1] == a[0,2] == x:
            return x 

    return None # None, 1 , 0 

    

#print( "- - - - - - - ")
#print( "winner:", check_if_solved(table))
#print( '-------------') 
