from pathlib import Path
import string

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

    return moving_cars_total, parked_cars, moving_cars

def make_list(moving_cars_total, parked_cars, moving_cars):
    ''' Liste Modell erstellen
    erstellt eine Liste in der Länge der Gesamtanzahl der geparkten Autos in parked_cars
    '''
    last_car = parked_cars[1]
    number = string.ascii_uppercase.index(last_car)

    model = [0] * (number + 1)
    print(model)

    for car in moving_cars:
        letter, number = car.split()
        if int(number) < len(model):
            model[int(number)] = 1
            model[int(number) + 1] = 1

        #wenn Auto auf letztem parkplatz steht, kann funktion so nicht ausgeführt werden -> edge cases prüfen !!!

    print(model)
    return (model)

if __name__ == '__main__':
    moving_cars_total, parked_cars, moving_cars = read_input()
    model = make_list(moving_cars_total, parked_cars, moving_cars)

