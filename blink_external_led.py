from machine import Pin
from utime import sleep

led = Pin(15, Pin.OUT)

while True:
    led.toggle()
    sleep(1)