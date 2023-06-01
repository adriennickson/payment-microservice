# https://raturi.in/blog/django-stripe-integration-fully-explained-example/
# https://stripe.com/docs/api?lang=python
# https://stripe.com/docs
# https://stripe.com/docs/testing

from decimal import Decimal

import stripe
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import CheckoutSessionRequestSerializer

stripe.api_key = settings.STRIPE_PRIVATE_KEY  # type: ignore


class StripeViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """

    @extend_schema(request=CheckoutSessionRequestSerializer)
    @action(detail=False, methods=["POST"])
    def create_checkout_session(self, request: Request) -> Response:
        # serializer = CheckoutSessionRequestSerializer(data=request.data)
        # if not serializer.is_valid():
        #     return Response({"message": "Ensure that price is greater than or equal to 0.50."}, status=500)

        session = stripe.checkout.Session.create(
            client_reference_id=f"{request.data['email']}__{request.data['platform']}",
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": request.data["currency"],
                        "product_data": {
                            "name": line_item["description"],
                        },
                        "unit_amount": int(100 * Decimal(line_item["price"])),
                    },
                    "quantity": line_item["quantity"],
                }
                for line_item in request.data["line_items"]
            ],
            mode="payment",
            success_url=request.data["success_url"],
            cancel_url=request.data["cancel_url"],
        )
        return Response({"id": session.id})

    @action(detail=False)
    def success(self, request):
        return Response({})

    @action(detail=False)
    def cancel(self, request):
        return Response({})

    @action(detail=False)
    def webhook(self, request):
        return Response({})


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
        success_url="http://127.0.0.1:8000/success/",
        cancel_url="http://127.0.0.1:8000/success/",
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
