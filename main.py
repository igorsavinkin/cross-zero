import check, random
import numpy as np
from output_arr import output
#from random import randint

def philip_robot(a, mark):
    
    opposite_mark = abs(mark - 1)
    for s in range(len(a)):
        for f in range(len(a[s])):
            if a[s,f] == mark:
                print('At row', s ,'and column ', f , 'there is mark:', mark)
            elif a[s,f] == opposite_mark:
                print('At row', s ,'and column ', f , 'there is opposite mark:', opposite_mark)
                

    c = random.randint(0,2)
    d = random.randint(0,2)
    while a[c, d] != '*':
        c = random.randint(0,2)
        d = random.randint(0,2)

    a[c, d] = mark
    print('Philip played [' ,c,  ',', d, ']')
    
    return a
        
def mark_robot(a, mark):
    opposite_mark = abs(mark - 1)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i,j] == mark:
                print('At row', i ,'and column ', j , 'there is mark:', mark)
            elif a[i,j] == opposite_mark:
                print('At row', i ,'and column ', j , 'there is opposite mark:', opposite_mark)
                

    x = random.randint(0,2)
    y = random.randint(0,2)                
    while a[x, y] != '*':
        x = random.randint(0,2)
        y = random.randint(0,2)
 
    a[x, y] = mark
    print('Mark played [', x, ',', y, ']')
 
    return a   

a = np.full([3, 3], "*", dtype=np.object)
#output(a)
start = input('Who starts? (f/m)')

if start.lower() == 'm':
    mark_mark=1 # отметка Марка
    philip_mark=0 # отметка Филиппа
    a = mark_robot(a, mark_mark) 
else:
    mark_mark=0
    philip_mark=1
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
        print ('winner:', winner)
        break
    output(a)
    print('===============================')
print('Final array:')
output(a)
#print ('winner:', check.check_if_solved(a))
