
def can_place_order(user, cart):
    if user is not None:
        if user["active"]:
            if len(cart) > 0:
                if user["age"] >= 18:
                    return True

    return False

# Aufgabe:

# Refactore die Funktion so, dass die verschachtelten `if`-Blöcke verschwinden 
# und die Logik leichter lesbar wird. Das Verhalten soll gleich bleiben.

def can_place_order(user, cart):
    if user is None:
        return False

    if not user["active"]:
        return False

    if not cart:
        return False

    if user["age"] < 18:
        return False

    return True

# Guard Clauses schützen den 
# eigentlichen Programmablauf vor Sonderfällen und reduzieren verschachtelte if-Blöcke.