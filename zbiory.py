# załóżmy, że pesel ma 4 cyfry
# stwórzmy zbiór NFZ – ludzie, w bazie pacjentów NFZ
# stwórzmy zbiór chorzy_rok – ludzie chorzy w ostatnim roku
# stwórzmy zbiór chorzy_miesiac – ludzie chorzy w ostatnim miesiącu
# stwórzmy zbiór krzyki – wszystkich ludzi mieszkających na krzykach
# stwórzmy zbiór centrum – wszystkich ludzi mieszkających

NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436])
chorzy_miesiac = {1234, 3476, 3098, 4544, 3423}
krzyki = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
centrum = {7648, 2345, 2356, 3987, 1234, 3476, 3254}
zbior_pusty = set()


#inetrsection - czesc wspolna
#ile osob chorowalo w ostatnim roku na krzykach

print('chorzy w ostatnim roku na Krzykach to =', krzyki.intersection(chorzy_rok))
print('Liczba =',len(krzyki.intersection(chorzy_rok)))

#sprawdzamy ile osob pracuje w centrum i na krzykach
#union - suma

print('w centrum i na krzykach mieszka', len(centrum.union(krzyki)), 'osob')

#diffrence - roznica dwoch zbiorow a.difference.b

if len(chorzy_miesiac.difference(chorzy_rok)) == 0:
    print('ok')
else:
    print('problem', chorzy_miesiac.difference(chorzy_rok))


#usuwanie ze zbioru

if len(krzyki.intersection(centrum)) != 0:
    x = input('usunac z centrum (c) czy z krzykow (k)?')
    duplikaty = krzyki.intersection(centrum)
    print(duplikaty)
    if x.lower() == 'k':
        krzyki = krzyki.difference(duplikaty)
    elif x.lower() == 'c':
        for pesel in duplikaty:
            centrum.remove(pesel)
    else:
        print('zly wybor')
    print('Sprawdzam duplikaty:', krzyki.intersection(centrum))

poza_NFZ = chorzy_rok.union(chorzy_miesiac.union(krzyki.union((centrum)))).difference(NFZ)

if len(poza_NFZ) != 0:
    print('Poza NFZ',poza_NFZ)
    NFZ = NFZ.union(poza_NFZ)
