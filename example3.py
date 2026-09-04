
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

