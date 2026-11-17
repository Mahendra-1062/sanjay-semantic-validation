def find_total(price, quantity):
    return price * quantity


def calculate_bulk_total(items):
    total = 0
    for price, quantity in items:
        total += find_total(price, quantity)
    return total


def calculate_final_price(price, quantity):
    return find_total(price, quantity)


def print_calculation(price, quantity):
    return find_total(price, quantity)