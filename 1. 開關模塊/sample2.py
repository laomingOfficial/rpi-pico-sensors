from machine import Pin
import time


button = Pin(19, Pin.IN, Pin.PULL_DOWN)
led = Pin(25, Pin.OUT)
delaySec = 0.3


while True:
    input_result = button.value()
    if input_result == True:
        led.toggle()

    time.sleep(delaySec)
