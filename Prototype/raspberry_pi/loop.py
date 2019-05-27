from threads import *
from queue import Queue

device_number = "<your_device_number>"
access_token = "<your_access_token>"

moisture_queue = Queue()

t_ping = PingThread(device_number, access_token)
t_moisture = MoistureThread(device_number, access_token, moisture_queue)
t_ping.start()
t_moisture.start()

# Main thread reports if plant needs watering
water = None
while True:
    if not moisture_queue.empty():
        moisture = moisture_queue.get()
        print("Moisture: ", moisture)

        if moisture < 1000 and (water == True or water is None):
            water = False
            water_plant(device_number, access_token, "water")
            print("\033[36mPlant needs watering\033[39m")
        if moisture > 1500 and (water == False or water is None):
            water = True
            water_plant(device_number, access_token, "stop")
            print("\033[36mPlant was watered\033[39m")
