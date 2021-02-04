from machine import Pin
import time

red = Pin(5, Pin.OUT)
yellow = Pin(6, Pin.OUT)


while True:
    ## 亮紅， 暗黃 = 紅
    #red.value(1)
    #yellow.value(0)
    
    # 亮紅， 暗黃 = 紅
    red.high()
    yellow.low()
    time.sleep(1)

    # 亮紅和黃 = 橙
    red.high()
    yellow.high()
    time.sleep(1)

    # 亮黃，暗紅 = 黃
    red.low()
    yellow.high()
    time.sleep(1)

    # 暗紅和黃 = 沒亮燈
    red.low()
    yellow.low()
    time.sleep(1)
