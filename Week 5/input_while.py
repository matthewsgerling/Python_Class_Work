# Program: basicLoops.py
# Author: Matthew Gerling
# Last date modified: 06/14/2020

x = 1
numbers = []

while x != 6:
    value = input('Please enter a number 1-100')
    if 0 > int(value) > 100:
        print('That is not an accepted value')
        break
    else:
        numbers.append(value)
        x = x + 1

print(numbers)
