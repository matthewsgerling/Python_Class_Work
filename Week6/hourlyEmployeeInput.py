# Program: hourlyEmployeeInput.py
# Author: Matthew Gerling
# Last date modified: 06/14/2020

def employeeInput() :
    name = input('Please enter Employee Name ')
    hour = input('Please enter Employee Hours ')
    payrate = input('Please enter Employee Pay Rate ')

    return print(name, 'worked', int(hour), 'hours with', float(payrate), 'pay.')


if __name__ == '__main__':
    try:  # check for ValueError
        employeeInput()  # function call
    except ValueError as err:
        print("ValueError encountered! ")
