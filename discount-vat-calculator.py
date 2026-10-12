"""
Day 6 - 2026-10-12
Tool: Discount & VAT Calculator
What it does: Works out the price after a percentage discount, adds VAT
on top, and shows how much money was saved - so a shopper can check a
sale price or a bill in seconds.
Who it helps: Anyone shopping during a sale, checking a restaurant or
shop bill with VAT, or comparing offers before buying.
"""


def price_after_discount(price, discount_percent):
    """Return the price after taking discount_percent off."""
    if price < 0:
        raise ValueError("Price cannot be negative.")
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount percent must be between 0 and 100.")
    return round(price * (1 - discount_percent / 100), 2)


def add_vat(price, vat_percent):
    """Return the price with vat_percent added on top."""
    if price < 0:
        raise ValueError("Price cannot be negative.")
    if vat_percent < 0:
        raise ValueError("VAT percent cannot be negative.")
    return round(price * (1 + vat_percent / 100), 2)


def amount_saved(price, discount_percent):
    """Return how much money the discount saves."""
    return round(price - price_after_discount(price, discount_percent), 2)


def final_price(price, discount_percent=0, vat_percent=0):
    """Discount first, then VAT on the discounted price."""
    return add_vat(price_after_discount(price, discount_percent), vat_percent)


if __name__ == "__main__":
    # Example 1: a shirt marked 1,200 taka with 25% off in a sale
    print("Shirt 1200, 25% off:", price_after_discount(1200, 25),
          "- you save", amount_saved(1200, 25))

    # Example 2: a phone at 18,500 taka, 10% discount, then 5% VAT
    print("Phone 18500, 10% off + 5% VAT:",
          final_price(18500, discount_percent=10, vat_percent=5))

    # Example 3: a restaurant bill of 2,400 taka with 15% VAT only
    print("Bill 2400 + 15% VAT:", add_vat(2400, 15))
