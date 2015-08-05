from decimal import Decimal as D


def apply_to(submission):

    def calculate_tax(price, rate):
        tax = price * rate
        return tax.quantize(D('0.01'))

    rate = D('0.20')
    for line in submission['basket'].all_lines():
        line_tax = calculate_tax(
            line.line_price_excl_tax_incl_discounts, rate)
        unit_tax = (line_tax / line.quantity).quantize(D('0.01'))
        line.purchase_info = unit_tax

    shipping_method = submission['shipping_method']
    shipping_method.tax = calculate_tax(
        shipping_method.charge_incl_tax, rate)
