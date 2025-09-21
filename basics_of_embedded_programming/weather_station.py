from machine import Pin
import dht, time

SENSOR_PIN = 15
d = dht.DHT22(Pin(SENSOR_PIN))

while True:
    try:
        d.measure()
        t = d.temperature()
        h = d.humidity()
        print("Temp: {:.1f} °C  |  Humidity: {:.1f} %".format(t, h))
    except OSError:
        print("Sensor read failed, retrying...")
    time.sleep(2)
