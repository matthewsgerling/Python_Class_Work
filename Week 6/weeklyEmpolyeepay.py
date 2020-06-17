# Program: weeklyemployeepay.py
# Author: Matthew Gerling
# Last date modified: 06/14/2020


def weeklyPay(x, y):
    return int(x) * float(y)


def employeeInput():
    name = input('Please enter Employee Name ')
    hour = input('Please enter Employee Hours ')
    payrate = input('Please enter Employee Pay Rate ')

    return name, "had a weekly pay of ", weeklyPay(hour, payrate)


if __name__ == '__main__':
    try:  # check for ValueError
        print(employeeInput())  # function call
    except ValueError as err:
        print("ValueError encountered! ")
