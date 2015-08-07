from decimal import Decimal as D
from collections import namedtuple
from oscar.apps.partner import strategy, prices
from indochine.apps.partner.models import TAXES


PurchaseInfo = namedtuple(
    'PurchaseInfo', ['price', 'availability', 'stockrecord'])


class Selector(object):
    def strategy(self, request=None, user=None, **kwargs):
        if request and 'stockrecords-0-fr_tax' in request.POST:
            if request.POST.get('stockrecords-0-fr_tax') == TAXES.FIVE_DOT_FIVE:
                return VAT550Strategy(request)
            elif request.POST.get('stockrecords-0-fr_tax') == TAXES.TEN:
                return VAT1000Strategy(request)
            elif request.POST.get('stockrecords-0-fr_tax') == TAXES.TWENTY:
                return VAT2000Strategy(request)
        return IndochineStrategy(request)


class IncludingVAT550(strategy.FixedRateTax):
    rate = D('0.055')


class IncludingVAT1000(strategy.FixedRateTax):
    rate = D('0.10')


class IncludingVAT2000(strategy.FixedRateTax):
    rate = D('0.20')

    def pricing_policy(self, product, stockrecord):
        if not stockrecord or stockrecord.price_excl_tax is None:
            return prices.Unavailable()

        return prices.FixedPrice(
            currency=stockrecord.price_currency,
            excl_tax=stockrecord.price_excl_tax,
            tax=D('0.00'))


class VAT550Strategy(strategy.UseFirstStockRecord, IncludingVAT550, strategy.Structured):
    """
    5.5% TAX
    """


class VAT1000Strategy(strategy.UseFirstStockRecord, IncludingVAT1000, strategy.Structured):
    """
    10% TAX
    """


class VAT2000Strategy(strategy.UseFirstStockRecord, IncludingVAT2000, strategy.Base):
    """
    20% TAX
    """


class IndochineStrategy(strategy.UseFirstStockRecord, strategy.Base):
    def fetch_for_product(self, product, stockrecord=None):
        if stockrecord is None:
            stockrecord = self.select_stockrecord(product)

        if stockrecord.fr_tax == TAXES.TWENTY:
            price = IncludingVAT2000.pricing_policy(product, stockrecord)

        return PurchaseInfo(
            price=price,
            availability=self.availability_policy(product, stockrecord),
            stockrecord=stockrecord)
