# Program: VariableAssignment.py
# Author: Matthew Gerling
# Last date modified: 06/2/2020


def convert_to_months(x):
    months = int(x) * 12
    return months


if __name__ == '__main__':
    age = input('Give an age for an infant (1-5 years)')

    print(convert_to_months(age))


