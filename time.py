import time

#מחזירה את הזמן הנוכחי בשניות מ1970
print(time.time())
#זמון השהייה לתוכנה
print(time.sleep(1))
#מפרק לגורמים את היום מהמחשב
print(time.localtime())
#מחזיר את התאריך כמחרוזת להדפסה למשתמש
print(time.asctime())
#זמן מקו המשווה
print(time.gmtime())
#מקבל זמן בשניות מ1970 ומחזירה מחרוזת להדפסה למשתמש
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


