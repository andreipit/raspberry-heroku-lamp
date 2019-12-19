#!/usr/bin/env python
# coding: utf-8

# In[1]:

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.OUT)
import urllib3, time
http = urllib3.PoolManager()

def set_lamp(value):
    print('lamp now is:', value)
    if value==0: GPIO.output(10, False)
    elif value==1: GPIO.output(10, True)
    return 

def send_to_web(value):
    if value==1:   http.request('GET', 'http://iot-flat-01.herokuapp.com/light_on_practice')
    elif value==0: http.request('GET', 'http://iot-flat-01.herokuapp.com/light_off_practice')
    print('sent to web:', value)
    return 

i = 0
while i < 1000: 
    r = http.request('GET', 'https://iot-flat-01.herokuapp.com/min')
    lamp_out = int(str(r.data)[3562:3563])
    set_lamp(lamp_out)
    send_to_web(lamp_out)
    time.sleep(1)
    i+=1
    


# In[ ]:


import datetime
str(datetime.datetime.now())
#datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)

# print(datetime.datetime.now())
# 2009-01-06 15:08:24.789150

