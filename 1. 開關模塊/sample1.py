from machine import Pin
import time


button = Pin(19, Pin.IN, Pin.PULL_DOWN)
led = Pin(25, Pin.OUT)
delaySec = 0.1


while True:
    input_result = button.value()
    led.value(input_result)
    print(input_result)
    time.sleep(delaySec)
