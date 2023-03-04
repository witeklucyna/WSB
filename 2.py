napis = 'Kamil ma psa'
lista_zwierzat = ['pies', 'drugi pies', 'tu tez pies']

print(napis[2:6])
print(lista_zwierzat[2]) # [2] element listy caly
print(lista_zwierzat[2][3])  #pierwszy 2 to element listy a potem 3 to wskazanie konkretnego indexu - slicing

print('nowa petla')

for i in range(3, 7):
    print(i)

print('nowa petla ze skokiem co 3 ')

for i in range(4, 20, 3):               #tu tez ta druga 3 to "skok" ,zakres 4-20, pokaze co 3
    print(i)

print('nowa petla ze skokiem co 3 ale od tylu, malejaco')

for i in range(20, 4, -3):  #od ,do, co ile - tu lecimy w dol stad -3
    print(i)


for i in range(4):
    print(napis)

for i in range(4):
    print('okrazenie ', i+1, ', a litera nr ',i+4,'to',napis[i+3], '\n')


for litera in napis:
    print(litera)

for zwierze in lista_zwierzat:
    print(zwierze)