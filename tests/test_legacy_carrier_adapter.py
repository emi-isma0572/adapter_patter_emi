from shipping_adapter.checkout import Checkout
from shipping_adapter.legacy_carrier import LegacyCarrier
from shipping_adapter.legacy_carrier_adapter import LegacyCarrierAdapter
from shipping_adapter.shipping_quote_provider import ShippingQuoteProvider


def test_checkout_can_quote_with_legacy_carrier_through_adapter():
    carrier = LegacyCarrier()
    adapter = LegacyCarrierAdapter(carrier)
    checkout = Checkout(adapter)

    assert isinstance(adapter, ShippingQuoteProvider)
    # 2 kg = 4.40924 lb; round(6.0 + 4.40924 * 1.25, 2) = 11.51
    assert checkout.shipping_quote("45000", 2.0) == 11.51
