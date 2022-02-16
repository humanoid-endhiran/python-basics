# Python Program to find sum of multi dimensional array in different methods

def findSum(l2d):
    #method 1
    tot=0
    for row in l2d:
        for c in row:
            tot  += c
    print("Method 1: {}".format(tot))

    #method 2
    tot =0
    for row in l2d:
        tot += sum(row)
    print("Method 2: {}".format(tot))

    #method 3
    sum(map(sum, l2d))
    print("Method 3: {}".format(tot))

    #method 4
    # note : best practice is to use import on top of the program.
    import numpy as np
    new_l2d = np.array(l2d)
    tot = sum(sum(new_l2d))
    print("Method 4: {}".format(tot))

l2d= [ [4,5,6], [8,9,10],[12,0,1]]

#mydict = {"m1": [4,5,6], "m2": [8,9,10], "m3": [12,0,1]}
print(l2d)


findSum(l2d)




