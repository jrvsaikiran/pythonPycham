import datetime
import time

a=time.time()
print("a=",a)

b=time.ctime(1655960314.4035196)
print("b=",b)

c=time.localtime()  #struct_time
print("c=",c)

d=time.mktime(c)
print("d=",d)

e=time.asctime(c)   #struct formate to local formate
print("e=",e)

f=time.strftime("%Y_%m_%d")
print("f=",f)

g=datetime.datetime.now()
print("g is",g)

h=datetime.timedelta(days=3)
print("h is",h)

i=g+h
print("i is",i)

print("====strftime=====")
help(time.strftime)

#help(time)

print("========from date============")
#from
date_now = datetime.datetime.today()        #today=now
print("set today date",date_now)

add_day= datetime.timedelta(days=7)
print("day is add",add_day)

set_date =date_now+add_day
print("set_date",set_date)

date_from = set_date.strftime(('%Y-%b-%d'))
print("date_from",date_from)

from_year = date_from.split("-")[0]
print("year is",from_year)

from_month = date_from.split("-")[1]
print("month is",from_month)

from_day = date_from.split("-")[2]
print("date is",from_day)


print("=====to date===========")

#to
date_to = datetime.datetime.now()+datetime.timedelta(days=20)
date_to = date_to.strftime(('%Y-%b-%d'))

to_year = date_to.split("-")[0]
print("year is",to_year)

to_month = date_to.split("-")[1]
print("month is",to_month)

to_day = date_to.split("-")[2]
print("date is",to_day)

