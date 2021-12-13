import time

print(time.time())
print(time.sleep(1))
print(time.localtime())
print(time.asctime())
print(time.gmtime())
print(time.ctime())
import datetime
#מראה עוד כמה זמן נשאר עד לתאריך שכתבנו
print(datetime.datetime(2030,1,1,00,1,1)-datetime.datetime.now())
#מוסיף ימים לתאריך הקיים
print(datetime.datetime.now()+datetime.timedelta(days=10))
x=datetime.datetime.now()+datetime.timedelta(days=10)
#מייצג את השעה בלבד
x.time()
print(x.time())
#מייצג את התאריך בלבד
x.date()
print(x.date())
#בודק איזה תאריך יותר גדול מהשני
print(datetime.datetime(2030,1,1,00,1,1)>datetime.datetime.now())
#המרת תאריך למחרוזת
now = datetime.datetime.now()
year=now.strftime("%Y")
print(f"year:{year}")


