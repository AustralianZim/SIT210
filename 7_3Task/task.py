import RPi.GPIO as gpio
import time

LED  = 33
TRIG = 11
ECHO = 12

gpio.setmode(gpio.BOARD)

gpio.setup(LED,  gpio.OUT)
gpio.setup(TRIG, gpio.OUT)
gpio.setup(ECHO, gpio.OUT)

led = gpio.PWM(LED, 100)
led.start(0) #start with 0% duty cycle

def distance():
    #send out a signal
    gpio.output(TRIG, 1)
    time.sleep(0.00001)
    gpio.output(TRIG, 0)

    start_time = time.time()
    stop_time = time.time()

    #get time of signal and arrival
    while gpio.input(ECHO) == 0:
        pass
        #start_time = time.time()
    while gpio.input(ECHO) == 1:
        stop_time = time.time()

    #calculate distance
    time_delta = stop_time - start_time
    distance = time_delta * 34300 / 2
    
    return distance

try:
    max_dist = 0
    while True:
        #calibrate and get distance
        if dist = distance() > max_dist:
            max_dist = dist
        print ("Distance: %d cm" % dist)

        #led brightness based on distance
        duty = dist / max_dist
        led.ChangeDutyCycle(duty)

        
except KeyboardInterrupt:
    gpio.cleanup()
