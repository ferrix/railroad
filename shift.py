from time import sleep
from collections import deque

from pi74HC595 import pi74HC595
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
shift_register = pi74HC595(16, 20, 21, 2)

values = deque([True] + [False] * 15)

try:
    while(True):
        shift_register.set_by_list(list(values))
        values.rotate(1)
        print("Enabling pin:", values.index(True))
        sleep(1)
except KeyboardInterrupt:
    gpio.cleanup()
    print("Ending happily")
