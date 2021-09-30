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


def make_list(parked_cars, moving_cars):
    # parkende Autos in eine Liste und bewegbare Autos in eine andere Liste.

    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    parkende_autos = []
    bewegliche_autos = []

    for letter in alphabet:
        ende = parked_cars[1]
        parkende_autos.append(letter)
        if letter == ende:
            break
    print(parkende_autos)

    n = 1

    while n < len(parkende_autos):
        bewegliche_autos.append("")
        n = n+1


    for car in moving_cars:
        name, number = car.split()
        print(name, number)

def move_moving_cars():
    # berechnet wie sich die Schiebeautos bewegen müssten, damit das gesuchte Auto ausparken kann.

    pass

def print_results():
    # gibt die Lösung aus.
    pass


if __name__ == '__main__':
    parked_cars, moving_cars = read_input()
    make_list(parked_cars, moving_cars)
