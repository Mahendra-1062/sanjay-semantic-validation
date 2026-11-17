from calculator import calculate_total


def get_order_total(price, quantity):
    return calculate_total(price, quantity)


def get_customer_total(price, quantity):
    return calculate_total(price, quantity)


def create_order(price, quantity):
    return {
        "total": calculate_total(price, quantity)
    }

def calculate_customer_invoice(price, quantity):
    return calculate_total(price, quantity)


def print_invoice(price, quantity):
    total = calculate_total(price, quantity)
    return f"Invoice total: {total}"