import smbus
import time

SENSOR  = 0x39
COMMAND = 0x80
CONTROL = 0x00
POWERON = 0x03
POWEROFF= 0x00
TIMING  = 0x01
CHANNEL0= 0x0C #IR + visible
CHANNEL1= 0x0E #IR


def setup():
    bus = smbus.SMBus(1)
    bus.write_byte_data(SENSOR, CONTROL | COMMAND, POWERON) #turn sensor on
    bus.write_byte_data(SENSOR, TIMING | COMMAND, 0x02) #nominal integration time = 402ms

    time.sleep(0.5) #wait some time to get ready
    return bus

def read_data(bus, channel):
    data = bus.read_i2c_block_data(SENSOR, channel | COMMAND, 2) #2 bytes

    #data is an array of bytes, so we need to convert this to an integer
    value = data[0] + data[1] * 256

    return value


bus = setup()
while(1):
    full_light = read_data(bus, CHANNEL0)
    infrared = read_data(bus, CHANNEL1)
    visible = full_light - infrared
    
    print("\033[38m---------------------\033[39m")
    print("\033[31mInfrared Light: %d lux\033[39m" % infrared)
    print("\033[33mVisible Light: %d lux\033[39m" % visible)
    print()

    time.sleep(0.5)
    
