from machine import Pin, PWM
import time

pwm_red = PWM(Pin(5, Pin.OUT))
pwm_yellow = PWM(Pin(6, Pin.OUT))
pwm_red.freq(100)
pwm_yellow.freq(100)

delaySec = 0.0001


while True:
    # 逐漸亮紅
    for dc in range(65025):
        pwm_red.duty_u16(dc)
        time.sleep(delaySec)

    # 逐漸暗紅
    for dc in range(65025, 0, -1):
        pwm_red.duty_u16(dc)
        time.sleep(delaySec)

    # 逐漸亮黃
    for dc in range(65025):
        pwm_yellow.duty_u16(dc)
        time.sleep(delaySec)

    # 逐漸暗黃
    for dc in range(65025, 0, -1):
        pwm_yellow.duty_u16(dc)
        time.sleep(delaySec)

    # 逐漸亮黃 同時 逐漸暗紅
    for dc in range(65025):
        pwm_yellow.duty_u16(dc)
        pwm_red.duty_u16(65025-dc)
        time.sleep(delaySec)

    # 逐漸暗黃 同時 逐漸亮紅
    for dc in range(65025, 0, -1):
        pwm_yellow.duty_u16(dc)
        pwm_red.duty_u16(65025-dc)
        time.sleep(delaySec)

    # 逐漸暗紅 同時 逐漸亮黃
    for dc in range(65025):
        pwm_red.duty_u16(dc)
        pwm_yellow.duty_u16(65025-dc)
        time.sleep(delaySec)

    # 逐漸亮紅 同時 逐漸暗黃
    for dc in range(0, 101, 5):
        pwm_red.duty_u16(dc)
        pwm_yellow.duty_u16(65025-dc)
        time.sleep(delaySec)
