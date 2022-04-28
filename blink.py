import machine
import time

led = machine.Pin(25, machine.Pin.OUT)

def blink(cant):
    for _ in range(99):
        led.on()
        time.sleep_ms(100)
        led.off()
        time.sleep_ms(100)