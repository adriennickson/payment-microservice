"""Core admin."""
from .customer import CustomerAdmin
from .order import OrderAdmin

__all__ = (
    "CustomerAdmin",
    "OrderAdmin",
)
