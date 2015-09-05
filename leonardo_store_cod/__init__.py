
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
        # patch checkout app where we override the payment details view
        from oscar.apps.checkout import app
        from cashondelivery.app import application as checkout_app
        from cashondelivery import views

        app.application = checkout_app
