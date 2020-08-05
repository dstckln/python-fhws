import datetime

def main():
   now = datetime.datetime.now()
   h = now.hour
   m = now.minute
   s = now.second

   midnight = now.replace(hour=0, minute=0, second=0)
   
   print("Sekunden seit Mitternacht: " + str((now - midnight).seconds))
   print("Sekunden bis Mitternacht: " + str(((24 - h - 1) * 60 * 60) + ((60 - m - 1) * 60) + (60 - s)))
   print("% des Tages vergangen: " + str((now - midnight).seconds * 100 / 86400))

if __name__ == "__main__":
    main() 
