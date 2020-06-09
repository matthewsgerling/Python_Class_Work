# Program: compoundExpressions.py
# Author: Matthew Gerling
# Last date modified: 06/9/2020

MAX = 10
MIN = 0
y = 5
x = 5

if y > MAX:
    print('True')
else:
    print('False')

if y < MIN:
    print('True')
else:
    print('False')

if x != MAX > x > MIN != x:
    print('True')
else:
    print('False')
if x != MAX > x >= MIN:
    print('True')
else:
    print('False')

if MAX >= x >= MIN:
    print('True')
else:
    print('False')
    