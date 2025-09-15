from machine import Pin
from utime import sleep

led = Pin("LED", Pin.OUT)

while True:
    led.toggle()
    sleep(1)