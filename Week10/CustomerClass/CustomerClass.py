# Author: Matthew Gerling
# File: CustomerClass.py
# Date: 7/1/2020


class Customer:

    def __init__(self, ID=0, fname='NA', lname='NA', pn='NA', add='NA'):
        self.customerId = ID
        self.lastName = lname
        self.firstName = fname
        self.phoneNumber = pn
        self.address = add

    def Display(self):
        if isinstance(self.customerId, int):
            print("Customer ID: ", self.customerId, ", Last Name: ", self.lastName, ", First Name: ", self.firstName,
                  ", Phone Number: ", self.phoneNumber, ", Address: ", self.address)
        else:
            print("AttributeError: 'Customer' object has no attribute 'cid'")


# Driver code
customer1 = Customer
customer1.Display()
customer2 = Customer
customer2 = Customer.__init__('100', 'Matt', 'Gerling', 'NA', 'NA')

