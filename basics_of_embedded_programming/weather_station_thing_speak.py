import network, time
from machine import Pin
import dht

try:
    import urequests as requests
except ImportError:
    import requests

SSID = "Wokwi-GUEST"
PASSWORD = ""

THINGSPEAK_WRITE_KEY = ""
UPDATE_PERIOD_S = 20
SENSOR_PIN = 15


def wifi_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to Wi-Fi…")
        wlan.connect(SSID, PASSWORD)
        t0 = time.ticks_ms()
        while not wlan.isconnected():
            if time.ticks_diff(time.ticks_ms(), t0) > 15000:
                raise RuntimeError("Wi-Fi timeout")
            time.sleep(0.2)
    print("Wi-Fi OK:", wlan.ifconfig()[0])


wifi_connect()

d = dht.DHT22(Pin(SENSOR_PIN))


def read_dht():
    for _ in range(3):
        try:
            d.measure()
            return d.temperature(), d.humidity()
        except OSError:
            time.sleep(0.5)
    return None, None


def push_thingspeak(temp_c, hum):
    url = (
        "http://api.thingspeak.com/update"
        "?api_key={key}&field1={t:.2f}&field2={h:.2f}"
    ).format(key=THINGSPEAK_WRITE_KEY, t=temp_c, h=hum)
    try:
        r = requests.get(url)
        entry_id = r.text
        r.close()
        return entry_id
    except Exception as e:
        print("ThingSpeak error:", e)
        return "0"


print("Pico W → ThingSpeak (Wokwi)")
while True:
    t, h = read_dht()
    if t is None:
        print("Sensor read failed, skipping.")
    else:
        print("Temp: {:.1f} °C | Humidity: {:.1f} %".format(t, h))
        eid = push_thingspeak(t, h)
        print("Uploaded. Entry ID:", eid)
    time.sleep(UPDATE_PERIOD_S)
