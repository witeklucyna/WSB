path = 'C://Users//vdi-student//Downloads//rozliczenie.csv'
mode = 'r'
with open(path, mode) as plik:
    content = plik.readlines()


print(content)
for i in range (len(content)):
    content[i] = content[i].split(',')
print(content)
print(content[i][1])


#rozliczanie sredniej wyplaty

total = 0
for i in range (1,len(content)): #zeby nie leciec od 0 - dajemy 1
    total += int(content[i][1]) # zamiast += mozna uzyc total +
average = total / (len(content) -1)
print(round(average,2))

#ile kobiet na miecierzynskim

total = 0
for i in range(1,len(content)):
    if content[i][3] == 'k' and content[i][4] == 't':
        total += 1
print(total)