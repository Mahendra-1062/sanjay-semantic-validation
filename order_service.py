from calculator import find_total


def get_order_total(price, quantity):
    return find_total(price, quantity)


def get_customer_total(price, quantity):
    return find_total(price, quantity)


def create_order(price, quantity):
    return {
        "total": find_total(price, quantity)
    }