from decimal import Decimal as D
from collections import namedtuple
from oscar.apps.partner import strategy
from indochine.apps.partner.models import TAXES


PurchaseInfo = namedtuple(
    'PurchaseInfo', ['price', 'availability', 'stockrecord'])


class Selector(object):
    def strategy(self, request=None, user=None, **kwargs):
        return FrStrategy(request)


class IncludingVAT550(strategy.FixedRateTax):
    rate = (TAXES.CHOICES_DICT[TAXES.FIVE_DOT_FIVE] / 100)


class IncludingVAT1000(strategy.FixedRateTax):
    rate = D(TAXES.CHOICES_DICT[TAXES.TEN] / 100)


class IncludingVAT2000(strategy.FixedRateTax):
    rate = D(TAXES.CHOICES_DICT[TAXES.TWENTY] / 100)


class FrStrategy(strategy.UseFirstStockRecord, strategy.Base, strategy.StockRequired):
    def fetch_for_product(self, product, stockrecord=None):
        if stockrecord is None:
            stockrecord = self.select_stockrecord(product)

        vat = strategy.Default()
        if stockrecord.fr_tax == TAXES.FIVE_DOT_FIVE:
            vat = IncludingVAT550()
        elif stockrecord.fr_tax == TAXES.TEN:
            vat = IncludingVAT1000()
        elif stockrecord.fr_tax == TAXES.TWENTY:
            vat = IncludingVAT2000()

        price = vat.pricing_policy(product, stockrecord)

        return PurchaseInfo(
            price=price,
            availability=self.availability_policy(product, stockrecord),
            stockrecord=stockrecord)
