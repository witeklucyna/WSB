import datetime

today = datetime.date.today()
print(type(today))
print(today)

data1 = today.strftime("Dzisiaj jest %d dzien ..... %m miesiaca")
data2 = today.strftime('%d--%m--%y')
print(data1)
print(data2)

now = datetime.datetime.now()
print(type(now))
print(now)

my_now = now.strftime('%M-%m-%S')
print(my_now)