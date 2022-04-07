import check, random
import numpy as np
from output_arr import output
#from random import randint

def philip_robot(a, mark):
    
    opposite_mark = abs(mark - 1)
    if a[1,1] == '*':
        a[1,1] = mark
        print('Philip puts smart move in the field center')                
        return a
##    for s in range(len(a)):
##        for f in range(len(a[s])):
##            if a[s,f] == mark:
##                print('At row', s ,'and column ', f , 'there is mark:', mark)
##            elif a[s,f] == opposite_mark:
##                print('At row', s ,'and column ', f , 'there is opposite mark:', opposite_mark) m
    # smart move check for horisontal move/win 
    for b in a:
        #print ('B: ', b)
        rowCouter = 0
        for elem in b:
            if elem == mark:
                rowCouter += 1
        for i in range(len(b)):
            if rowCouter == 2 and b[i] =="*":
                b[i] = mark
                print ('Philip played smart move for row')
                return a
            
    #  smart move check for vertical move/winp
    # a[:,0] - 1-й столбец.
    # a[:, i] - i-й столбец.
    for i in range(a.shape[1]):
        #print('столбец:', i, ': ' , a[:, i])
        # a[:, i] 
        columnCouter = 0
        for elem in a[:, i]:
            if elem == mark:
                columnCouter += 1
        for j in range(a.shape[0]):
            if columnCouter == 2 and a[j][i] =="*":
                a[j][i] = mark
                print ('Philip played smart move for column')
                return a
 
    #проверка диагоналей
    diagonalCounter = 0
    for  u in range(a.shape[1]):       
        if a[u,u] == mark:
            diagonalCounter += 1
    if diagonalCounter == 2:
        for  u in range(a.shape[1]):       
            if a[u,u] == "*":
                a [u,u]= mark
                print ('Philip played smart move for diagonal')
                return a
    ######################## BLOCKAGE ##########################
    # блокировка соперника
    # in row
    for i in range(a.shape[1]):
        b = a[i]
        rowCounter = 0 
        for j in range(len(b)):
            if b[j] == opposite_mark:
                 rowCounter += 1 
        for j in range(len(b)):
            if rowCounter == 2 and b[j] == "*": 
                b[j] = mark
                print('Philip blocked other player with a smart move for row: [', i,',', j, ']')
                return a
    # in column
    for i in range(a.shape[1]):
        #print('столбец:', i, ': ' , a[:, i])
        # a[:, i] 
        columnCouter = 0
        for elem in a[:, i]:
            if elem == opposite_mark:
                columnCouter += 1
        for j in range(a.shape[0]):
            if columnCouter == 2 and a[j][i] =="*":
                a[j][i] = mark
                print ('Philip blocked other player with a smart move for column: [', j,',', i, ']')
                return a
    # in the main diagonal 
    diagonalCounter = 0
    for  u in range(a.shape[1]):       
        if a[u,u] == opposite_mark :
            diagonalCounter += 1
    if diagonalCounter == 2:
        for  u in range(a.shape[1]):       
            if a[u,u] == "*":
                a [u,u]= mark
                print ('Philip blocked other player with a smart move for diagonal:  [', u,',', u, ']')
                return a
    if a[0,0] == '*':
        a[0,0] = mark
        print('Philip puts smart move in the field corner')                
        return a
    
    if a[0,2] == '*':
        a[0,2] = mark
        print('Philip puts smart move in the field corner')                
        return a

    if a[2,2] == '*':
        a[2,2] = mark
        print('Philip puts smart move in the field corner')                
        return a

    if a[2,0] == '*':
        a[2,0] = mark
        print('Philip puts smart move in the field corner')                
        return a
            
    # random move
    c = random.randint(0,2)
    d = random.randint(0,2)
    while a[c, d] != '*':
        c = random.randint(0,2)
        d = random.randint(0,2)

    a[c, d] = mark
    print('Philip plays random [' ,c,  ',', d, ']')
    
    return a
        
def mark_robot(a, mark):
    opposite_mark = abs(mark - 1)
    # put in the center if vacant
    if a[1,1] == '*':
        a[1,1] = mark
        print('Mark puts smart move in the field center')                
        return a
        
    
    
    # smart move check for horisontal move
    for i in range(a.shape[1]):
        b = a[i]
        rowCounter = 0 
        for j in range(len(b)):
            if b[j] == mark:
                 rowCounter += 1 
        for j in range(len(b)):
            if rowCounter == 2 and b[j] == "*": 
                b[j] = mark
                print('Mark plays smart move for row: [', i,',', j, ']')
                return a

        #  smart move check for vertical move/winp
    # a[:,0] - 1-й столбец.
    # a[:, i] - i-й столбец.
    for i in range(a.shape[1]):
        #print('столбец:', i, ': ' , a[:, i])
        # a[:, i] 
        columnCouter = 0
        for elem in a[:, i]:
            if elem == mark:
                columnCouter += 1
        for j in range(a.shape[0]):
            if columnCouter == 2 and a[j][i] =="*":
                a[j][i] = mark
                print ('Mark played smart move for column')
                return a

        #проверка диагоналей
    diagonalCounter = 0
    for  u in range(a.shape[1]):       
        if a[u,u] == mark:
            diagonalCounter += 1
    if diagonalCounter == 2:
        for  u in range(a.shape[1]):       
            if a[u,u] == "*":
                a [u,u]= mark
                print ('Mark played smart move for diagonal')
                return a

            
 ######################## BLOCKAGE ##########################
    # блокировка соперника
    # in row
    for i in range(a.shape[1]):
        b = a[i]
        rowCounter = 0 
        for j in range(len(b)):
            if b[j] == opposite_mark:
                 rowCounter += 1 
        for j in range(len(b)):
            if rowCounter == 2 and b[j] == "*": 
                b[j] = mark
                print('Mark blocked other player with a smart move for row: [', i,',', j, ']')
                return a
    # in column
    for i in range(a.shape[1]):
        #print('столбец:', i, ': ' , a[:, i])
        # a[:, i] 
        columnCouter = 0
        for elem in a[:, i]:
            if elem == opposite_mark:
                columnCouter += 1
        for j in range(a.shape[0]):
            if columnCouter == 2 and a[j][i] =="*":
                a[j][i] = mark
                print ('Mark blocked other player with a smart move for column: [', j,',', i, ']')
                return a
    # in the main diagonal 
    diagonalCounter = 0
    for  u in range(a.shape[1]):       
        if a[u,u] == opposite_mark :
            diagonalCounter += 1
    if diagonalCounter == 2:
        for  u in range(a.shape[1]):       
            if a[u,u] == "*":
                a [u,u]= mark
                print ('Mark blocked other player with a smart move for diagonal:  [', u,',', u, ']')
                return a

    if a[0,0] == '*':
        a[0,0] = mark
        print('Mark puts smart move in the field corner')                
        return a
    
    if a[0,2] == '*':
        a[0,2] = mark
        print('Mark puts smart move in the field corner')                
        return a

    if a[2,2] == '*':
        a[2,2] = mark
        print('Mark puts smart move in the field corner')                
        return a

    if a[2,0] == '*':
        a[2,0] = mark
        print('Mark puts smart move in the field corner')                
        return a


          
    
##    for i in range(len(a)):
##        for j in range(len(a[i])):
##            if a[i,j] == mark:
##                print('At row', i ,'and column ', j , 'there is mark:', mark)
##            elif a[i,j] == opposite_mark:
##                print('At row', i ,'and column ', j , 'there is opposite mark:', opposite_mark)
               
    # random move
    x = random.randint(0,2) # int - integer - целое
    y = random.randint(0,2)                
    while a[x, y] != '*':
        x = random.randint(0,2)
        y = random.randint(0,2)
 
    a[x, y] = mark
    print('Mark plays random [', x, ',', y, ']')
 
    return a

def check_if_end(a):
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            if a[i,j] == "*":
                return False
    return True 
                
            
        
        

    
## ********************* Beginning *****************************
## Beginning 
a = np.full([3, 3], "*", dtype=np.object)
#output(a)

print ("================================================")
#print ("Initial array:")
#output(a) 
start = input('Who starts? PHILIP or MARK: (p/m)')

if start.lower() == 'm':
    mark_mark=1 # отметка Марка
    philip_mark=0 # отметка Филиппа
    print('Филипп играет за ', philip_mark )
    print('Марк играет за ', mark_mark )
    print('===============================')
    a = mark_robot(a, mark_mark)
    players = {1: 'Mark', 0: 'Philip'}
    output(a) 
    print('===============================')
    
else:
    mark_mark=0
    philip_mark=1
    print('Филипп играет за ', philip_mark )
    print('Марк играет за ', mark_mark )
    print('===============================')
    players = {0: 'Mark', 1: 'Philip'}
 
result = None
for x in range(100):
    a = philip_robot(a, philip_mark)
    winner = check.check_if_solved(a)
    if winner != None:
        print ('The winner:', players[winner],"*_*")
        break
    output(a)
    if check_if_end(a):
        print ('The draw, no more moves to do.')
        exit()
    
    a = mark_robot(a, mark_mark)
    winner = check.check_if_solved(a)
    if winner != None:
        print ('The winner:',players[winner],"*_*")
        break
    output(a)
    if check_if_end(a):
        print ('The draw, no more moves to do.')
        exit()
    print('===============================')
    
print('Final array:')
output(a)
#print ('winner:', check.check_if_solved(aprint(players[]

