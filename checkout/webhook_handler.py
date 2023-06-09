from django.http import HttpResponse


class StripeWH_handler:
    """Handler Stripe webhook"""

    def __init__(self, request):
        self.request = request

    def handler_event(self, event):
        """
        Handle a generic/unknown/inexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)
    
    def handler_payment_intent_succeeded(self, event):
        """
        Handle a payement_intent_succeeded webhook from stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
    
    def handler_payment_intent_payment_failed(self, event):
        """
        Handle a payement_intent_payment_failed webhook from stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
