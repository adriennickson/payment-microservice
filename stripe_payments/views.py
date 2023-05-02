# https://raturi.in/blog/django-stripe-integration-fully-explained-example/#:~:text=Stripe%20is%20integrated%20with%20Django,passed%20to%20the%20front%20end.
# https://stripe.com/docs/api?lang=python
# https://stripe.com/docs
# https://stripe.com/docs/testing

import stripe
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_PRIVATE_KEY
YOUR_DOMAIN = "http://127.0.0.1:8000"


@csrf_exempt
def create_checkout_session(request):
    session = stripe.checkout.Session.create(
        client_reference_id="madriennickson@gmail.com__EKWALI",
        payment_method_types=["card"],
        line_items=[
            {
                "price_data": {
                    "currency": "eur",
                    "product_data": {
                        "name": "Intro to Django Course",
                    },
                    "unit_amount": 100,
                },
                "quantity": 2,
            },
            {
                "price_data": {
                    "currency": "eur",
                    "product_data": {
                        "name": "Lorem ipsum",
                    },
                    "unit_amount": 1000,
                },
                "quantity": 5,
            },
        ],
        mode="payment",
        success_url=YOUR_DOMAIN + "/success/",
        cancel_url=YOUR_DOMAIN + "/cancel/",
    )
    return JsonResponse({"id": session.id})


# home view
def home(request):
    return render(request, "stripe_payments/checkout.html")


# success view
def success(request):
    return render(request, "stripe_payments/success.html")


# cancel view
def cancel(request):
    return render(request, "stripe_payments/cancel.html")


@csrf_exempt
def webhook(request):
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
    event = None

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except ValueError:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event["type"] == "checkout.session.completed":
        # print("Payment was successful.")
        # print(event["client_reference_id"])
        pass
    # _TODO: run some custom code here

    return HttpResponse(status=200)
