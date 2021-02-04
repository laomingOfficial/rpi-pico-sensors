from machine import Pin, PWM
import time

pwm_red = PWM(Pin(5, Pin.OUT))
pwm_green = PWM(Pin(6, Pin.OUT))
pwm_blue = PWM(Pin(13, Pin.OUT))
pwm_red.freq(100)
pwm_green.freq(100)
pwm_blue.freq(100)

delaySec = 0.0001

while True:
    for i in range(65025):
        pos = i
        if pos < 21675:
            pwm_red.duty_u16(pos*3)
            pwm_green.duty_u16(65025-pos*3)
            pwm_blue.duty_u16(0)
        elif pos < 43350:
            pos -= 21675
            pwm_red.duty_u16(65025-pos*3)
            pwm_green.duty_u16(0)
            pwm_blue.duty_u16(pos*3)
        else:
            pos -= 43350
            pwm_red.duty_u16(0)
            pwm_green.duty_u16(pos*3)
            pwm_blue.duty_u16(65025-pos*3)
        time.sleep(delaySec)
