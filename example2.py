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


# Die Funktion funktioniert, macht aber eigentlich **drei Dinge**:

# - Gesamtpreis berechnen
# - Rabatt anwenden
# - Ausgabe erzeugen

def calculate_total(items):
    """ """
    total = 0

    for item in items:
        total += item["price"] * item["quantity"]

    return total


def apply_discount(total):
    if total > 100:
        return total * 0.9

    return total


def print_order_summary(customer_name, items, total):
    print("Kunde:", customer_name)
    print("Anzahl Positionen:", len(items))
    print("Gesamtpreis:", total)


def create_order(customer_name, items):
    total = calculate_total(items)
    total = apply_discount(total)

    print_order_summary(customer_name, items, total)

    return total