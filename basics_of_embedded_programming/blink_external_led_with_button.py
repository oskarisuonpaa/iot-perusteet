from machine import Pin

led = Pin(18, Pin.OUT)
switch = Pin(13, Pin.IN, Pin.PULL_UP)

while True:
    if switch.value():
        led.value(False)
    else:
        led.value(True)