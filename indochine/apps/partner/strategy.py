from decimal import Decimal as D
from oscar.apps.partner import strategy


class Selector(object):
    """
    Custom selector to return a FR-specific strategy that charges VAT
    """

    def strategy(self, request=None, user=None, **kwargs):
        return FRStrategy()


class IncludingVAT(strategy.FixedRateTax):
    """
    Price policy to charge VAT on the base price
    """
    rate = D('0.20')


class FRStrategy(strategy.UseFirstStockRecord, IncludingVAT,
                 strategy.StockRequired, strategy.Structured):
    pass
