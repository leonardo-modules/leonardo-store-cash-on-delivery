
from import_export import resources

from cashondelivery.models import CashOnDeliveryTransaction


class CashOnDeliveryTransactionResource(resources.ModelResource):

    class Meta:
        model = CashOnDeliveryTransaction
