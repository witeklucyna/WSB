import datetime

today = datetime.date.today()
print(type(today))
print(today)

data1 = today.strftime("Dzisiaj jest %d dzien ..... %m miesiaca")
data2 = today.strftime('%d--%m--%y')
print(data1)
print(data2)