#n = 3 
#arr = [['*'] * n for i in range(n)]
#print(a)

def output(a):
    for row in a:
        for elem in row:
            print(str(elem).center(3), end=' ')
        print()

#arr[1][1] = 106
#arr[1][2] = None
#arr[2][2] = None
#output(arr) 
