from invoice_master.backend import Invoice
from invoice_master.frontend.base import BaseInvoiceInterface

class InvoiceCreationInterface(BaseInvoiceInterface):
    def create_invoice(self, items):
        invoice = Invoice(items)
        self.display_invoice(invoice)

    def display_invoice(self, invoice):
        print(f'Total: {invoice.rounded_total}$')