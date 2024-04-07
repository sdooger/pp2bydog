#TSIS 4 Date

#ex1
from datetime import date,timedelta

today = date.today()
after = today-timedelta(days=5)
print(after)

#ex2
today = date.today()
yesterday = today-timedelta(days=1)
tomorrow = today+timedelta(days=1)
print(yesterday,today,tomorrow)

#ex3
mics = datetime.now()
mics = mics.replace(microsecond=0)
print(mics)

#ex4
from datetime import datetime,timedelta
cur_date = datetime.now()

new_date = cur_date-timedelta(days=1)

print(cur_date,new_date,sep="\n")