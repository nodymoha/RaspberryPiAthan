import time
from pygame import mixer
import string
import praytimes
from datetime import date
athan_sound = 'makkah.mp3'
latitude = 00.00
longitude = 00.00
timezone = 0

while (1):

        tmm = praytimes.PrayTimes().getTimes(date.today(),[latitude,longitude],timezone)
        FAJR=tmm['fajr']
        DHUHR=tmm['dhuhr']
        ASR=tmm['asr']
        MAGHRIB=tmm['maghrib']
        ISHA=tmm['isha']

	
        tempT= time.strftime(str('%H'))
        currTime= tempT
        tempT= time.strftime(str('%M'))
        currTime= currTime +':'+ tempT
        if currTime == FAJR:
                print('Fajr athan')
                mixer.init(16000)
                mixer.music.load(athan_sound)
                mixer.music.play()
                while mixer.music.get_busy() == True:
                        continue
        if currTime == DHUHR:
                print('Dhuhr athan')
                mixer.init(16000)
                mixer.music.load(athan_sound)
                mixer.music.play()
                while mixer.music.get_busy() == True:
                        continue
        if currTime == ASR:
                print('Asr athan')
                mixer.init(16000)
                mixer.music.load(athan_sound)
                mixer.music.play()
                while mixer.music.get_busy() == True:
                        continue
        if currTime == MAGHRIB:
                print('Maghrib athan')
                mixer.init(16000)
                mixer.music.load(athan_sound)
                mixer.music.play()
                while mixer.music.get_busy() == True:
                        continue
        if currTime == ISHA:
                print('Isha athan')
                mixer.init(16000)
                mixer.music.load(athan_sound)
                mixer.music.play()
                while mixer.music.get_busy() == True:
                        continue
        time.sleep(1)
        
