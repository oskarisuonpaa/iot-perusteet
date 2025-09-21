from machine import Pin
import utime, urandom

led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

state = "idle"
off_time_us = 0
reaction_us = None
too_soon = False
_last_irq_ms = 0
pressed_flag = False


def on_button_irq(pin):
    global state, off_time_us, reaction_us, _last_irq_ms, too_soon, pressed_flag
    now_ms = utime.ticks_ms()
    if utime.ticks_diff(now_ms, _last_irq_ms) < 50:
        return
    _last_irq_ms = now_ms

    if pin.value() == 1:
        pressed_flag = True
        if state == "armed":
            too_soon = True
            state = "idle"
        elif state == "ready" and reaction_us is None:
            reaction_us = utime.ticks_diff(utime.ticks_us(), off_time_us)
            state = "idle"


button.irq(trigger=Pin.IRQ_FALLING, handler=on_button_irq)


def random_delay_ms(min_ms=1500, max_ms=4000):
    span = max_ms - min_ms
    return min_ms + (urandom.getrandbits(16) % (span + 1))


print("Reaction Game: wait for the LED to turn OFF, then press the button!")

while True:
    reaction_us = None
    too_soon = False
    pressed_flag = False

    led.on()
    state = "armed"
    print("\nReady... wait.")

    utime.sleep_ms(random_delay_ms())
    led.off()
    off_time_us = utime.ticks_us()
    state = "ready"

    while state != "idle":
        if pressed_flag:
            pressed_flag = False

        utime.sleep_ms(5)

    if too_soon:
        print("Too early! Wait for the LED to turn OFF before pressing.")
    else:
        print("Reaction time: {:.2f} ms".format(reaction_us / 1000))

    utime.sleep_ms(1200)
