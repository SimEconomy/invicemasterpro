from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, HiddenField
from wtforms.validators import DataRequired, NumberRange

class InvoiceForm(FlaskForm):
    customer_name = StringField('Customer Name', validators=[DataRequired()])
    item_description = StringField('Item Description', validators=[DataRequired()])
    quantity = DecimalField('Quantity', validators=[DataRequired(), NumberRange(min=0)])
    unit_price = DecimalField('Unit Price', validators=[DataRequired(), NumberRange(min=0)])
    calculate_total = HiddenField()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    form = InvoiceForm()
    if form.validate_on_submit():
        total = form.quantity.data * form.unit_price.data
        return f'Total: {total}'
    return render_template('invoice_form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)