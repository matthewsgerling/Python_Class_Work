# Program: multiplyString.py
# Author: Matthew Gerling
# Last date modified: 06/14/2020


def multiplyString():
    string = input('Enter a string to multiply')
    multiply = input('how many times to multiply')
    return print(str(string) * int(multiply))


if __name__ == '__main__':
    multiplyString()
