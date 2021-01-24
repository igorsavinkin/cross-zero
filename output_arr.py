#print()
#arr= [['*'], []]
n = 3 
arr = [['*'] * n for i in range(n)]
#print(a)

def output(a):
    for row in a:
        for elem in row:
            print(str(elem).rjust(2), end=' ')
        print()

arr[1][1] = 10   
output(arr)
#print(7897, 'hi'.rjust(100))
