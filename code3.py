def total_per_fellow(transactions):
    totals = {}

    for transaction in transactions:
        fellow = transaction["fellow"]
        quantity = transaction["quantity"]

        if fellow not in totals:
            totals[fellow] = 0

        totals[fellow] += quantity

    return total