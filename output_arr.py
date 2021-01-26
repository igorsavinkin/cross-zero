def output(a):
    for row in a:
        for elem in row:
            print(str(elem).center(3), end=' ')
        print()
