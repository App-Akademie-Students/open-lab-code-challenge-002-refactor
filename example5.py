def calculate_price(customer_type, price):
    if customer_type == "premium":
        return price * 0.9

    elif customer_type == "student":
        return price * 0.8

    elif customer_type == "business":
        return price * 0.85

    return price


# Das Problem: Mit jedem neuen Kundentyp wächst die if/elif-Kette weiter.

# Aufgabe

# Ersetze die Fallunterscheidung durch Polymorphie. Jeder Kundentyp soll seine eigene Preislogik
# 
#  besitzen.

