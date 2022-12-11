path = 'C:\\Users\\vdi-student\\WSB\\rozliczenie.csv'
mode = 'r'
with open(path, mode) as plik:
    content = plik.readlines() #cos.cos to metoda - nie funkcja. na tym pliku z 3 linii przeczytaj wszystkie linie i zapisz w content
print(content[3])


for i in range (len(content)):
    #print(content[i])
    content[i] = content[i].split(',') #wez kolejna linie, )tyle linii ile len) , czyli content[0],[1] itp i podziel ja
    print(content[i])


#rozliczanie sredniej wyplaty

print('\nRozliczenie średniej wypłaty')
total = 0 #wartosc pocztkowa, potem po len bedziemy do niej dodawac +1
for i in range (1, len(content)): #zeby nie leciec od 0 - dajemy 1
    total += int(content[i][1]) # zamiast += mozna uzyc total + content[i][1] bo wynagrodzenie to druga kolumna|| z defaultu to co mamy w pliku python widzi jako string, stad int, ale moze warto float?
average = total / (len(content)-1)
print(round(average,2))

#inny przyklad

# print('\nInny przyklad')
# for i in range(15):
#     print(i)
#
# print('\nJeszcze inny przyklad') # przeanalizowac czemu printuje dziwne rzeczy
# for i in range(15, 3 ,-2):
#     print(i)

#ile kobiet na miecierzynskim

print('\nLiczba kobiet na urlopie macierzyńskim')

total = 0
for i in range(1,len(content)):
    print(content[i]) #widac ze mamy znak konca linii \n
    content[i][4] = content[i][4].replace('\n','')
    if content[i][4] == 't':
        total += 1 #zwieksz o 1
print(total)