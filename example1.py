
# Was würdet ihr hier refactoren – ohne das Verhalten des Programms zu verändern?
def calculate_price(quantity, base_price, customer_type):
    if customer_type == "premium":
        x = quantity * base_price
        if x > 100:
            x = x * 0.9
        print("Preis:", x)
        return x

    if customer_type == "standard":
        x = quantity * base_price
        if x > 100:
            x = x - 5
        print("Preis:", x)
        return x

    if customer_type == "student":
        x = quantity * base_price
        x = x * 0.8
        print("Preis:", x)
        return x

    print("Unbekannter Kundentyp")
    return 0
