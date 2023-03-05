# jak najprosciej usunac duplikaty z listy

lista = [1, 2, 3, 3, 3, 4, 4, 5, 5, 6]

lista = list(set(lista))
print(lista)