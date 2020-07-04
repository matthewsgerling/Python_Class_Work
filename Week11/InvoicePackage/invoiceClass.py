# Author: Matthew Gerling
# File: invoiceClass.py
# Date: 7/3/2020

from Week11.CustomerPackage.CustomerClass import Customer


class Invoice:
    def __init__(self, iid, customerInfo):
        self.Customer = customerInfo
        self.invoice_id = iid
        self.items_with_price: dict = {}

    def add_item(self, item):
        self.items_with_price.update(item)

    def create_invoice(self):
        print('Invoice #', self.invoice_id, '\n', self.Customer.Display(), '\n', self.items_with_price)


# Driver
captain_mal = Customer(1, 'Reynolds', 'Mel', 'No phones', 'Firefly, somewhere in the verse')
invoice = Invoice(1, captain_mal)
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.create_invoice()
