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

from abc import ABC, abstractmethod


class Customer(ABC):

    @abstractmethod
    def calculate_price(self, price):
        pass


class PremiumCustomer(Customer):
    def calculate_price(self, price):
        return price * 0.9

class StudentCustomer(Customer):
    def calculate_price(self, price):
        return price * 0.8

class BusinessCustomer(Customer):
    def calculate_price(self, price):
        return price * 0.85

class RegularCustomer(Customer):
    def calculate_price(self, price):
        return price


def checkout(customer, price):
    return customer.calculate_price(price)
customer1 = PremiumCustomer()
customer2 = StudentCustomer()

price1 = checkout(customer1, 100)
price2 = checkout(customer2, 100)