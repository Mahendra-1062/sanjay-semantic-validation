
from calculator import calculate_total


def get_order_total(price, quantity):
    """
    Get the total amount for an order.
    """
    return calculate_total(price, quantity)


def get_customer_total(price, quantity):
    """
    Get the total amount for a customer.
    """
    return calculate_total(price, quantity)


def create_order(user_id, price, quantity):
    """
    Create an order for a user.
    """
    total = calculate_total(price, quantity)

    return {
        "user_id": user_id,
        "price": price,
        "quantity": quantity,
        "total": total
    }
