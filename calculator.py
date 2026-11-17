def calculate_total(price, quantity, tax_percentage):
    """
    Calculate total price including tax.
    """
    subtotal = price * quantity
    tax = subtotal * tax_percentage / 100
    return subtotal + tax


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
