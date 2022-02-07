#!/usr/local/bin/python
'''
This example processes a multi dimenstional list and  display only negative numbers.

Key concepts used:
Uses the filter() out only negative numbers
Uses apend() to add elements to list
Converts a multi dimensional list to a single dimensional list using sum()

'''
def display_neg(n):

    if n<0:
        return n



l2d=[ [0,1,-1],[-4,1,6],[8,1,-1]]
negl=[]
for row in range(len(l2d)):
    negl.append(list(filter(display_neg,l2d[row])))
print (sum(negl, []))

'''
output:
[-1, -4, -1]
'''
