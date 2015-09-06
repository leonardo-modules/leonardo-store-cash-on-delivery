
from cashondelivery.views import PaymentDetailsView
from django.utils.translation import ugettext as _
from leonardo_store.payments.methods import PaymentMethod


class CashOnDeliveryPaymentMethod(PaymentMethod):
    code = 'cod'
    name = _('Cash on Delivery')
    description = _('Cash on Delivery')

    view = PaymentDetailsView
