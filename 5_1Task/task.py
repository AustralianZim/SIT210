import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(10, gpio.OUT)

try:
    while 1:
        gpio.output(10, 1)
        time.sleep(0.15)
        gpio.output(10, 0)
        time.sleep(0.5)
except KeyboardInterrupt:
    gpio.cleanup()
