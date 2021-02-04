from machine import Pin
import time


red = Pin(5, Pin.OUT)
green = Pin(6, Pin.OUT)
blue = Pin(13, Pin.OUT)


while True:
    # 亮紅， 暗綠和藍 = 紅                                                                                                                                                                                                                       
    red.high()
    green.low()
    blue.low()
    time.sleep(1)

    # 亮紅和綠， 暗藍 = 黃
    red.high()
    green.high()
    blue.low()
    time.sleep(1)

    # 亮綠， 暗紅和藍 = 綠
    red.low()
    green.high()
    blue.low()
    time.sleep(1)

    # 亮綠和藍， 暗紅 = 淺藍？
    red.low()
    green.high()
    blue.high()
    time.sleep(1)

    # 亮藍， 暗綠和紅 = 藍
    red.low()
    green.low()
    blue.high()
    time.sleep(1)

    # 亮紅和藍， 暗綠 = 粉紅
    red.high()
    green.low()
    blue.high()
    time.sleep(1)

    # 亮紅和藍和綠 = 白
    red.high()
    green.high()
    blue.high()
    time.sleep(1)

    # 暗紅和藍和綠 = 沒亮燈
    red.low()
    green.low()
    blue.low()
    time.sleep(1)
