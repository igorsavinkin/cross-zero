import check, random
import numpy as np
#from random import randint

def philip_robot(a, mark):
    
    x=1
    y=1
    if a[x, y] == '*':
        a[x][y] = mark
        print('Philip played [' ,x,  ',', y, ']')
    else:
        pass
    return a
        
def mark_robot(a, mark):   
    x = random.randint(0,2)
    y = random.randint(0,2)
    
    if a[x, y] == '*':
        a[x, y] = mark
        print('Mark played [', x, ',', y, ']')
    else:
        pass
    return a   
def output_array(a):
    pass

    
#a = np.array([[None, None, None],
#              [None, None, None],
#              [None, None, None]])
#a = np.array([[None, None, None],
#              [None, None, None],
#              [None, None, None]])
a = np.full([3, 3], "*", dtype=np.object)
print(a)
start = input('Who starts? (f/m)')

if start.lower() == 'm':
    mark_mark=1 # отметка Марка
    philip_mark=0 # отметка Филиппа
    a = mark_robot(a, mark_mark) 
else:
    mark_mark=0
    philip_mark=1
print(a)
print('Филипп ставит:', philip_mark )
print('Марк ставит:', mark_mark )
print('===============================')
#exit()   
result = None
for x in range(10):
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
    print(a)
    print('===============================')
print('Final array:\n', a)
#print ('winner:', check.check_if_solved(a))
