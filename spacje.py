nazwa = ' Kamil Adam Musial'
# nazwa_ze_zmiana = nazwa.replace('i', 'DUZE_I', 1)  #co,na co, ilerazy
#
# print(nazwa_ze_zmiana)
#
# nazwa_bez_spacji = nazwa.replace(' ', '')
# print(nazwa_bez_spacji)
#
# print(nazwa.replace(' ', '\n'))


nazwa_podzielona = nazwa.split()
print(nazwa_podzielona)
for slowo in nazwa_podzielona:
    print(slowo)

print('najszybsze rozwiazanie i najbardziej zwiezle: ')

for slowo in nazwa.split():
    print(slowo)