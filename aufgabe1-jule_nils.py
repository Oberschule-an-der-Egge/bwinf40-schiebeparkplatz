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
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    reihe1 = []
    reihe2 = []

    for letter in alphabet:
        ende = parked_cars[1]
        reihe1.append(letter)
        if letter == ende:
            break
    print(reihe1)

    print(moving_cars[0])



if __name__ == '__main__':
    parked_cars, moving_cars = read_input()
    make_list(parked_cars, moving_cars)
