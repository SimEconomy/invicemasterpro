from decimal import Decimal, ROUND_HALF_UP

class Invoice:
    def __init__(self, items):
        self.items = items
        self.total = self.calculate_total()
        self.rounded_total = self.round_total()

    def calculate_total(self):
        total = Decimal(0)
        for item in self.items:
            total += item['price'] * Decimal(item['quantity'])
        return total

    def round_total(self):
        return total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)