import time
from subprocess import Popen, PIPE
import os

def alarm_clock():
  prompt = raw_input('In what time do you want to HH:MM:SS\n>')
  hour, minute, second = prompt.split(':')
  now = time.localtime()

  t = (now.tm_year, now.tm_mon, now.tm_mday, int(hour), int(minute), int(second),-1,-1, -1)
  
  alarm_time = time.mktime(t)
  sleep_time = alarm_time - time.mktime(now)
  
  time.sleep(sleep_time)
  print ('ALARM! ALARM! ALARM! ALARM!') #until music comes
 
  
  
  
  
  
alarm_clock()
  