import datetime
import time

name = 'raport.txt'
for i in range(10):
    now = datetime.datetime.now()
    my_now = now.strftime('%H%M%S')
    print(name[:6] + my_now + name[-4:])
    time.sleep(2)