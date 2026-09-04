def create_customer(name, street, city, zip_code):
    print("Kunde:", name)
    print("Adresse:", street, city, zip_code)


def create_invoice(name, street, city, zip_code, amount):
    print("Rechnung für:", name)
    print("Adresse:", street, city, zip_code)
    print("Betrag:", amount)


def send_delivery(name, street, city, zip_code):
    print("Lieferung an:", name)
    print("Adresse:", street, city, zip_code)


# Aufgabe

# Erkenne zusammengehörige Daten, 
# die immer wieder gemeinsam auftreten, und refactore sie zu einer eigenen Struktur.
