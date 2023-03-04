import time


def welcome_basic():
    time.sleep(1.5)
    print('przyotowywanie obrazu systemu')
    time.sleep(1.5)
    print('sprawdzanie bledow w systemie')
    time.sleep(1.5)
    print("siema")

def welcome_full(imie, wiek):
    if wiek >= 18 :
        print('Dzien dobry',imie)
    else:
        print('czesc',imie)


def stan_zdrowia(waga,wzrost):
    BMI = waga / (wzrost**2)
    if BMI > 35:
        return 1
    elif BMI > 20:
        return 2
    return 3    #nie musi byc else, jesli funkcja trafi raz na return nie bedzie szla dalej, wiec nie ma ryzyka ze petla if sie wywali


