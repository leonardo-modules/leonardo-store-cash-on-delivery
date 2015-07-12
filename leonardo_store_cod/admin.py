from django.contrib import admin
from cashondelivery.models import CashOnDeliveryTransaction
from leonardo_import_export.admin import ImportExportModelAdmin
from cashondelivery.admin import CashOnDeliveryTransactionAdmin
from .resources import CashOnDeliveryTransactionResource


class CashOnDeliveryTransactionAdmin(
        CashOnDeliveryTransactionAdmin, ImportExportModelAdmin):
    resource = CashOnDeliveryTransactionResource

admin.site.unregister(CashOnDeliveryTransaction)
admin.site.register(CashOnDeliveryTransaction, CashOnDeliveryTransactionAdmin)
