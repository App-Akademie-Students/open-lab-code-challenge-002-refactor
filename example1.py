
# Was würdet ihr hier refactoren – ohne das Verhalten des Programms zu verändern?
def calculate_price(quantity, base_price, customer_type):
    price = quantity * base_price

    if customer_type == "premium":
        if price > 100:
            price *= 0.9
    elif customer_type == "standard":
        if price > 100:
            price -= 5
    elif customer_type == "student":
        price *= 0.8
    else:
        print("Unbekannter Kundentyp")
        return 0

    print("Preis:", price)
    return price
# Duplikate entfernen
# sprechende Namen verwenden
# verantwortlichkeiten trnnen
# Bedingungen vereinfachen
# 
