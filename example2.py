def create_order(customer_name, items):
    
    total = 0

    for item in items:
        total += item["price"] * item["quantity"]

    if total > 100:
        total *= 0.9

    print("Kunde:", customer_name)
    print("Anzahl Positionen:", len(items))
    print("Gesamtpreis:", total)

    return total