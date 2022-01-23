import check, random
import numpy as np
from output_arr import output
#from random import randint

def philip_robot(a, mark):
    
    opposite_mark = abs(mark - 1)
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

    # smart move check for horisontal move
    for i in range(len(a)):
        b = a[i]
        rowCounter = 0 
        for j in range(len(b)):
            if b[j]==mark:
                 rowCounter += 1 
        for j in range(len(b)):
            if rowCounter == 2 and b[j] == "*": 
                b[j] = mark
                print('Mark plays smart move for row: [', i, ', ', j, ']')
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


## ********************* Beginning *****************************
## Beginning 
a = np.full([3, 3], "*", dtype=np.object)
#output(a)

print ("================================================")
print ("Initial array:")
output(a) 
start = input('Who starts? PHILIP or MARK: (p/m)')

if start.lower() == 'm':
    mark_mark=1 # отметка Марка
    philip_mark=0 # отметка Филиппа
    a = mark_robot(a, mark_mark)
    players = {1: 'Mark', 0: 'Philip'}
else:
    mark_mark=0
    philip_mark=1
    players = {0: 'Mark', 1: 'Philip'}
#a[0,0]= mark
output(a) 

print('Филипп ставит:', philip_mark )
print('Марк ставит:', mark_mark )
print('===============================')
#exit()   
result = None
for x in range(100):
    a = philip_robot(a, philip_mark)
    winner = check.check_if_solved(a)
    if winner != None:
        print ('winner:', winner)
        break
    a = mark_robot(a, mark_mark)
    winner = check.check_if_solved(a)
    if winner != None:
        print ('The winner:', winner)
        break
    output(a)
    print('===============================')
print('Final array:')
output(a)
#print ('winner:', check.check_if_solved(a))
