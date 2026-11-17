
def calculate_total(price, quantity):
    """
    Calculate the total price before tax.

    Args:
        price: Price per item.
        quantity: Number of items.

    Returns:
        Total price before tax.
    """
    return price * quantity


def calculate_bulk_total(price, quantity):
    """
    Calculate the total for bulk purchases.
    """
    return calculate_total(price, quantity)


def calculate_final_price(price, quantity):
    """
    Calculate the final price before any additional processing.
    """
    return calculate_total(price, quantity)


def print_calculation(price, quantity):
    """
    Print the calculated total.
    """
    total = calculate_total(price, quantity)
    print(f"Total: {total}")
    return total
