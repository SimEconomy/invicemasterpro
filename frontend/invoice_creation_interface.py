from invoice_master.frontend.base import InvoiceInterface

class InvoiceCreationInterface(InvoiceInterface):
    def __init__(self):
        super().__init__()
        self.create_invoice_button = self.add_button('Create Invoice')
        self.invoice_details_area = self.add_area('Invoice Details')
        self.total_amount_label = self.add_label('Total Amount: $0.00')
        self.calculate_button = self.add_button('Calculate Total')
        self.items_list = self.add_list('Invoice Items')
    def add_invoice_item(self, description, quantity, price):
        item_dict = {
            'description': description,
            'quantity': quantity,
            'price': price
        }
        self.items_list.append(item_dict)
        self.calculate_total_amount()
    def calculate_total_amount(self):
        total = 0
        for item in self.items_list:
            total += item['quantity'] * item['price']
        self.total_amount_label.text = f'Total Amount: ${total:.2f}'