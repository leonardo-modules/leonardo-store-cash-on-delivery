
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
        from feincms.views.decorators import standalone

        app.application = checkout_app
        # mark handle as standalone
        views.PaymentDetailsView.handle_payment_details_submission = standalone(
            views.PaymentDetailsView.handle_payment_details_submission)
