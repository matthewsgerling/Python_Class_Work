# Author: Matthew Gerling
# File: invoiceClass.py
# Date: 7/1/2020


class Invoice:
    def __init__(self, iid, cid, ln, fn, pn, add):
        self.invoice_id = iid
        self.customer_id = cid
        self.last_name = ln
        self.first_name = fn
        self.phone_number = pn
        self.address = add
        self.items_with_price: dict = {}

    def add_item(self, item):
        self.items_with_price.update(item)

    def create_invoice(self):
        print(self.first_name, ', ', self.last_name, ' ,', self.customer_id , ' : ', self.invoice_id, ' ,', self.phone_number
              , ' ,', self.address, ' ,', self.items_with_price)


# Driver code
invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802', 'Mouse', 'Minnie', '555-867-5309')
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.create_invoice()
