# Author: Matthew Gerling
# File: customExceptions.py
# Date: 7/1/2020
from Week12.customExceptions.testCustomExpectations import InvalidCustomerIdException, InvalidNameException, \
    InvalidPhoneNumberFormat


class Customer:

    def __init__(self, ID=0, fname='NA', lname='NA', pn=1234567890):
        if 1000 < ID < 9999:
            self.customerId = ID
        else:
            print(InvalidCustomerIdException)

        if lname.isalpha():
            self.lastName = lname
        else:
            print(InvalidNameException)
        if fname.isalpha():
            self.firstName = fname
        else:
            print(InvalidNameException)

        if len(str(pn)) == 10:
            self.phoneNumber = pn
        else:
            print(InvalidPhoneNumberFormat)

    def Display(self):
        if isinstance(self.customerId, int):
            print("Customer ID: ", self.customerId, ", Last Name: ", self.lastName, ", First Name: ", self.firstName,
                  ", Phone Number: ", self.phoneNumber,)
        else:
            print("AttributeError: 'Customer' object has no attribute 'cid'")


# Driver code
c1 = Customer(1372, 'Matt', 'Gerling', 1231231234)
c2 = Customer(999, 'Matt!', 'Gerling2', 123456789)
try:
    c1.Display()
    c2.Display()
except InvalidCustomerIdException:
    print('Not Valid CID')
try:
    c1.Display()
    c2.Display()
except InvalidNameException:
    print('Not Valid Name')

try:
    c1.Display()
    c2.Display()
except InvalidNameException:
    print('Not Valid Name')

try:
    c1.Display()
    c2.Display()
except InvalidPhoneNumberFormat:
    print('Not Valid Number Format')


