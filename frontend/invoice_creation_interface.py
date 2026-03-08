from invoice_master.frontend import InvoiceCreationInterface

# Implement initial UI design
invoice_creation_interface = InvoiceCreationInterface()

# Example function to add invoice item
def add_invoice_item(item_name, item_cost, quantity):
    invoice_creation_interface.add_item(item_name, item_cost, quantity)

# Example function to calculate total
def calculate_total(invoice_items):
    total = 0
    for item in invoice_items:
        total += item['cost'] * item['quantity']
    return round(total, 2)

def setup_invoice_creation_interface():
    # Implement UI setup and initialization
    pass