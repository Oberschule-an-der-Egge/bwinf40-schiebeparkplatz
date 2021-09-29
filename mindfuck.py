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

    return

def parkinglot():

    parkinglot = ["A", "B", "C", "D", "E", "F", "G"]

    h = 2
    i = 5

    for space in parkinglot:
        index = parkinglot.index(space)
        print(index)
        if index in [h, h + 1, i, i + 1]:
            print("besetzt\n")
            #move_cars()
        else:
            print("frei\n")


def move_cars(index):
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



if __name__ == '__main__':
    read_input()
    parkinglot()
