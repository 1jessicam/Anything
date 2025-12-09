import datetime as dt
class Clock:
    def __init__(self,alarms = []):
        self.alarms = alarms
        self.old_time = dt.datetime.now().strftime("%I:%M %p")

    def get_time(self):
        return dt.datetime.now().strftime("%I:%M %p")
    
    def get_hours(self):
        return dt.datetime.now().strftime("%I")
    
    def get_hours(self):
        return dt.datetime.now().strftime("%M")
    
    def get_hours(self):
        return dt.datetime.now().strftime("%S")
    
    def time_change(self,time):
        return self.old_time != time


time = Clock()
def main():
    while True:
        rn = time.get_time()
        if time.time_change(rn):
            time.old_time = rn
            print(rn)

main()


