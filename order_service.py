from calculator import calculate_total


def get_order_total(price, quantity):
    return calculate_total(price, quantity)


def get_customer_total(price, quantity):
    return calculate_total(price, quantity)


def create_order(price, quantity):
    print(f"Creating order with price: {price} and quantity: {quantity}")
    return {
        "total": calculate_total(price, quantity),
        "sum": calculate_total(price + quantity, price - quantity)
    }