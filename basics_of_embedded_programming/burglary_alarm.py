from machine import Pin
import utime

pir = Pin(28, Pin.IN)

while True:
    if pir.value() == 1:
        print("Burglar alert!")
        utime.sleep(1)
    else:
        utime.sleep(1)
