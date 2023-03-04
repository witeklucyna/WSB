from funkcje2 import  *
#
#
# imie = 'Kasia'
# print(len(imie))
# number = 2343.2356
# print(round(number, 2))
#
#
# welcome_basic()
#
#
# imie1 = 'Marysia'
# lista_imion = ['Adam', 'Marek']
#
# welcome_full('Waldemar', 38)
# welcome_full(imie1, 12)
# welcome_full(lista_imion[1], 94)
#
# print(stan_zdrowia(75, 1.75))

licznik = 0
while True:
    wyplata = input('Ile zarabiasz? ')
    try:
        wyplata = float(wyplata)
        break
    except ValueError:
        print('zle dane,jeszcze raz - podaj kwote liczbowo')
        licznik += 1
    if licznik == 3:
        print('wyplata 2000')
        wyplata = 2000
        break

while True:
    liczba_dzieci = int(input('Ile masz dzieci? ' ))
    try:
        liczba_dzieci = int(liczba_dzieci)
        break
    except ValueError:
        print('zle dane,jeszcze raz')


try:
    print('kasa na dziecko =', wyplata / (liczba_dzieci))
except ZeroDivisionError:
    print('cala kasa dla ciebie')