from invoice_master.frontend import create_invoice

from flask import render_template

# Function to render the invoice creation interface
@create_invoice.route('/create_invoice', methods=['GET'])
def create_invoice_interface():
    return render_template('create_invoice.html')
