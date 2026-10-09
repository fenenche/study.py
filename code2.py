def borrow(resource, quantity):
    if quantity > resource["available"]:
        return "Not enough stock"

    resource["available"] -= quantity
    return "Success"