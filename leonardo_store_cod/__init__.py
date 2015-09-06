
from django.apps import AppConfig

default_app_config = 'leonardo_store_cod.Config'

LEONARDO_APPS = [
    'leonardo_store_cod',
    'cashondelivery',
]


class Config(AppConfig):
    name = 'leonardo_store_cod'
    verbose_name = ("Cash on Delivery")

    def ready(self):

        # register payment method
        from cashondelivery.methods import *
