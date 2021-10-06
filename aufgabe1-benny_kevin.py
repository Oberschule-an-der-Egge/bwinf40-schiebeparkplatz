from pathlib import Path


def read_input(filename='parkplatz0.txt'):
    """ Beispieldatei einlesen
    Die Zeilen in Integer und List umwandeln und Zeilenumbrüche mit .strip() entfernen.
    Default ist das Aufgabenbeispiel parkplatz0.txt.
    """
    file = Path('beispieldaten', filename)
    with open(file, 'r') as file_in:
        parked_cars = file_in.readline().split()
        moving_cars_total = file_in.readline().strip()
        moving_cars = [line.strip() for line in file_in.readlines()]


    return parked_cars, moving_cars_total, moving_cars


def make_list(parked_cars, moving_cars_total, moving_cars):
    """ Listen erstellen
    Das Alphabet durchgehen (Buchstabe für Buchstabe) und wenn "buchstabe" == "ende" ist wird der Loop beendet.
    Der Loop fragt ab ob "buchstabe" == "ende" entspricht. "ende" ist der zweite Wert von "parked_cars".
    """
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    ende = parked_cars[1]
    liste_parkend = []
    liste_bewegend = []


    for buchstabe in alphabet:
        liste_parkend.append(buchstabe)
        if buchstabe == ende:
            break
    print(liste_parkend)

    for auto in liste_parkend:
        liste_bewegend.append(0)

    for auto in moving_cars:
        buchstabe, zahl = auto.split()
        zahl = int(zahl)
        liste_bewegend[zahl] = 1
        liste_bewegend[zahl + 1] = 1



    print(liste_bewegend)





def make_result():
    """Ergebnis berechnen
    """
    pass



def print_result():
    """Das Ergebnis wird ausgegeben, um anzuzeigen, welche Autos verschoben werden müssen.
    """
    pass
    dict = {"A": "frei",
            "B": "frei"}






if __name__ == '__main__':
    parked_cars, moving_cars_total, moving_cars = read_input()
    make_list(parked_cars, moving_cars_total, moving_cars)
    print_result()
    make_result()
