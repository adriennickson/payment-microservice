from django.test import TestCase


class StripeTest(TestCase):
    def test_should_create_stripe_checkout_session(self):
        data = {
            "email": "user@example.com",
            "platform": "lezing",
            "currency": "xaf",
            "line_items": [
                {"quantity": 1, "description": "Lorem ipsum", "price": "2.99"},
                {"quantity": 2, "description": "Lorem ipsum", "price": "4.99"},
            ],
            "success_url": "http://127.0.0.1:8000/success/",
            "cancel_url": "http://127.0.0.1:8000/cancel/",
        }

        response = self.client.post(
            "/api/v1/payment/stripe/create_checkout_session/",
            data,
            format="json",
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue("id" in response.data)
