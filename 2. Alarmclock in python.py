from datetime import datetime
from playsound import playsound

alarmtime = input('Enter the alarm time (HH:MM:SS AM/PM):\n')

alarmhour = int(alarmtime[0:2])
alarmminute = int(alarmtime[3:5])
alarmsecond = int(alarmtime[6:8])
alarmperiod = alarmtime[9:11].upper()

while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime('%M')
    current_second = now.strftime('%S')
    current_period = now.strftime('%p')

    if alarmperiod == current_period:
        if alarmhour == current_hour:
            if alarmminute == current_minute:
                if alarmsecond == current_second:
                    print('Wake Up Shailesh Vishwakarma')
                    playsound('audio.mp3')
                    break
