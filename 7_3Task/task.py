import RPi.GPIO as gpio
import time

LED  = 33
TRIG = 11
ECHO = 12

gpio.setmode(gpio.BOARD)

gpio.setup(LED,  gpio.OUT)
gpio.setup(TRIG, gpio.OUT)
gpio.setup(ECHO, gpio.IN)

led = gpio.PWM(LED, 100)
led.start(0) #start with 0% duty cycle

def distance():
    #send out a signal
    gpio.output(TRIG, 1)
    time.sleep(0.001)
    gpio.output(TRIG, 0)

    start_time = time.time()
    stop_time = time.time()

    #get time of signal and arrival
    while gpio.input(ECHO) == 0:
        start_time = time.time()
    while gpio.input(ECHO) == 1:
        if stop_time - start_time > 0.05:
            break
        stop_time = time.time()

    #calculate distance
    time_delta = stop_time - start_time
    distance = time_delta * 34300 / 2
    
    return distance

try:
    max_dist = 200
    dist = 100
    while True:
        
        new_dist = distance()
        if new_dist - dist < 400 and new_dist - dist > -400:
            dist = new_dist
        
        print ("Distance: %d cm" % dist)

        #led brightness based on distance
        duty = dist / max_dist
        if duty > 1:
            duty = 1
        led.ChangeDutyCycle(90*duty)
        print ("Duty: %d" % duty)
        
except KeyboardInterrupt:
    gpio.cleanup()
