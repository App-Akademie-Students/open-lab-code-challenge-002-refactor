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

from dataclasses import dataclass
@dataclass
class Address:
    street: str
    city: str
    zip_code: str



def create_customer(name, address:Address):
    print("Kunde:", name)
    print("Adresse:", address.street, address.city, address.zip_code)


def create_invoice(name, address, amount):
    print("Rechnung für:", name)
    print("Adresse:", address.street, address.city, address.zip_code)
    print("Betrag:", amount)


def send_delivery(name, address):
    print("Lieferung an:", name)
    print("Adresse:", address.street, address.city, address.zip_code)

    #Verwendung
    address = Address(
    street="Hauptstraße 10",
    city="Berlin",
    zip_code="10115"
)
address = Address(
    street="Hauptstraße 10",
    city="Berlin",
    zip_code="10115"
)
create_customer("Anna", address)
create_invoice("Anna", address, 149.90)
send_delivery("Anna", address)

# Was noch?
