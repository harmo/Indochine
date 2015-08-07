from decimal import Decimal as D
from oscar.apps.partner import strategy
from indochine.apps.partner.models import TAXES


class Selector(object):
    def strategy(self, request=None, user=None, **kwargs):
        if request and 'stockrecords-1-fr_tax' in request.POST:
            if request.POST.get('stockrecords-1-fr_tax') == TAXES.FIVE_DOT_FIVE:
                return IncludingVAT550
            elif request.POST.get('stockrecords-1-fr_tax') == TAXES.TEN:
                return IncludingVAT1000
        return IncludingVAT2000


class IncludingVAT550(strategy.FixedRateTax):
    rate = D('0.055')


class IncludingVAT1000(strategy.FixedRateTax):
    rate = D('0.10')


class IncludingVAT2000(strategy.FixedRateTax):
    rate = D('0.20')


class VAT550Strategy(strategy.UseFirstStockRecord, IncludingVAT550,
                    strategy.StockRequired, strategy.Structured):
    pass


class VAT1000Strategy(strategy.UseFirstStockRecord, IncludingVAT1000,
                    strategy.StockRequired, strategy.Structured):
    pass


class VAT2000Strategy(strategy.UseFirstStockRecord, IncludingVAT2000,
                    strategy.StockRequired, strategy.Structured):
    pass
