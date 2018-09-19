from datetime import datetime, timedelta, date 
dt_now=datetime.now()
print(dt_now)
delta=timedelta(days=31)
print(delta)
previous_time=dt_now-delta
print(previous_time)

#Превратите строку "01/01/17 12:10:03.234567" в объект datetime
date_string='01/01/17 12:10:03.234567'
date_object=datetime.strptime(date_string, '%m/%d/%Y %H:%M:%S')
print(date_object)