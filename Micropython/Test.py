from machine import Pin
import time

gpio_pin = Pin(20, Pin.OUT)

def pulse(pin, high_time, low_time):
    """
    Geef een puls op de pin:
    Maak de pin pin_nr hoog, wacht high_time,
    maak de pin laag, en wacht nog low_time
    """
    pin.on()             # Zet de pin hoog
    time.sleep(high_time) # Wacht voor de opgegeven hoog-tijd
    pin.off()            # Zet de pin laag
    time.sleep(low_time)  # Wacht voor de opgegeven laag-tijd

while True:
    pulse(gpio_pin, 0.2, 0.2)
