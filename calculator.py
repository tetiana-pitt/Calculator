# from functions import summe, multipl, substr
# from functions.arithmetics import summe, subtraktion, multiplikation
import sys
from functions import arithmetics
from functions import geo

print(sys.path)

# from functions import summe    negativ beispiele_ könnte konflikt mit anderen funktionen geben
# from functions.arithmetics import *   negativ beispiel. nicht alles importieren

# konstanten in Python werden große geschrieben. Konvention!
OPERATIONS = {
    '+': arithmetics.summe,
    '*': arithmetics.multiplikation,
    '-': arithmetics.subtraktion,
    '/': arithmetics.divi,
    '**': arithmetics.square,
    'dist': geo.distance,
}


def sum():  # ich überschreibe Original von python sum()
    print("ich bin jetzt die Funktion sum")


def parse_user_input(user_input):
    """Zerlege den userinput in seine Bestandteile
    Beispiel Userinput: + 3 43
    Args:
        user_input(str): die Usereingabe
    Returns:
        tuple: (operator, operand, operand)
    """
    user_input = user_input.split()  # ['+', '3', '43']
    operator = user_input.pop(0)
    a, b = float(user_input[0]), float(user_input[1])

    return operator, a, b


def controller(operator, a, b):
    op = OPERATIONS.get(operator)
    if op:
        return op(a, b)
    raise NotImplementedError("Diese Operation ist nicht implementiert")


def main():
    """Hauptprogramm. Hier wird der User-Input verarbeitet"""

    while True:
        msg = "Bitte Berechnung ein: (Operator und 2 Operatoren): "
        user_input = input(msg)
        
        if user_input in ["_quit", "_exit"]:
            print("Danke. Programm beendet")
            break

        operator, a, b = parse_user_input(user_input)
        result = controller(operator, a, b)
        print("Ergebnis: ", result)


main()
