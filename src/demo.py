from shipping_adapter.checkout import Checkout
from shipping_adapter.legacy_carrier import LegacyCarrier
from shipping_adapter.legacy_carrier_adapter import LegacyCarrierAdapter


def main() -> None:
    carrier = LegacyCarrier()
    adapter = LegacyCarrierAdapter(carrier)
    checkout = Checkout(adapter)

    price = checkout.shipping_quote("45000", 2.0)
    print(f"Shipping quote: {price:.2f}")


if __name__ == "__main__":
    main()
