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

    print(parked_cars)
    print(moving_cars_total)
    print(moving_cars)

    return parked_cars, moving_cars


def make_parkinglot(moving_cars):
    """
    Die Funktion parkinglot() gibt den Autos auf dem Parkplatz einen Index und prüft, welche Autos ausparken können und
    welche nicht.
    """

    parkinglot = ["A", "B", "C", "D", "E", "F", "G"]

    occupiedlot = {}

    for element in moving_cars:
        letter, number = element.split()
        number = int(number)
        occupiedlot[letter] = number
        occupiedlot[letter.lower()] = number + 1
        print(occupiedlot)

    for space in parkinglot:
        index = parkinglot.index(space)
        if index in occupiedlot.values():
            print(f"{parkinglot[index]}: besetzt\n")
            #move_cars(occupiedlot, index)
        else:
            print(f"{parkinglot[index]}: frei")


def move_cars(index, occupiedlot):
    """
    Die Funktion move_cars() prüft, wie die Autos, die im Weg stehen, verschoben werden müssen, damit die Autos auf den Parkplätzen
    ausparken können.
    """

    while index in [h, h + 1, i, i + 1]:
        if index == h:
            check = h + 2
            if check == i:
                h -= 2
            else:
                h += 2
        elif index == h + 1:
            check = h + 3
            if check == i:
                h -= 1
            else:
                h += 3
        elif index == i:
            pass
        elif index == i + 1:
            pass


def print_result():
    """
    Zeigt die Rangieranweisungen als Lösung an.
    """
    pass

if __name__ == '__main__':
    parked_cars, moving_cars = read_input()
    make_parkinglot(moving_cars)
    print_result()
