from django.db import models
from extended_choices import Choices
from oscar.apps.partner.abstract_models import AbstractStockRecord as CoreAbstractStockRecord


TAXES = Choices(
    ('NONE', 0, ''),
    ('FIVE_DOT_FIVE', 1, 5.5),
    ('TEN', 2, 10),
    ('TWENTY', 3, 20)
)


class StockRecord(CoreAbstractStockRecord):
    fr_tax = models.IntegerField(choices=TAXES, default=TAXES.TWENTY, verbose_name='Taxe')


from oscar.apps.partner.models import *  # noqa
