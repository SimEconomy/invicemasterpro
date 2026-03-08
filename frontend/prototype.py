from invoice_master.frontend import BaseInvoice

# Function to create a simple prototype
def create_prototype():
    invoice = BaseInvoice()
    invoice.item_description = 'Sample Item'
    invoice.price = 120.00
    invoice.quantity = 1
    invoice.calculate_total()
    return invoice

# Prototype creation example
prototype_invoice = create_prototype()
print(prototype_invoice total)