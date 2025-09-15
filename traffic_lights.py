from machine import Pin
from utime import sleep, sleep_ms

leds = [Pin(15, Pin.OUT), Pin(14, Pin.OUT), Pin(13, Pin.OUT)]  # RED, YELLOW, GREEN
buzzer = Pin(12, Pin.OUT)
switch = Pin(16, Pin.IN, Pin.PULL_DOWN)

def sequentally_turn_leds_on():
    for led in leds:
        led.value(1)
        sleep(1)

def sequentally_turn_leds_off():
    for led in leds:
        led.value(0)
        sleep(1)

def handle_switch():
    leds[0].value(1)
    buzzer.value(1)
    sleep(5)
    leds[0].value(0)
    buzzer.value(0)

while True:
    if switch.value():
        handle_switch()
    sequentally_turn_leds_on()
    sequentally_turn_leds_off()
        
