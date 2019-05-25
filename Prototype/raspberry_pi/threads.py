from funcs import *
from datetime import datetime
from time import sleep
import threading

class PingThread(threading.Thread):
    def __init__(self, device_number, access_token):
        threading.Thread.__init__(self)
        self.device_number = device_number
        self.access_token = access_token
        self.isOnline = None

    def run(self):
        #run indefinitely
        while True:
            try:
                result = ping_particle(self.device_number, self.access_token) #ping Photon and store the result (bool)
                
                #If the status changes, report to console
                if self.isOnline != result or self.isOnline is None:
                    self.isOnline = result
                    if self.isOnline:
                        print("\033[36mParticle \033[32mONLINE\033[39m")
                    else:
                        print("\033[36mParticle \033[31mOFFLINE\033[39m")
                        
                        sleep (5)
            except Exception as e:
                print("Ping Error: ", e.text)
                sleep(60)
                print("Trying again...")
                    

class MoistureThread(threading.Thread):
    def __init__(self, device_number, access_token, moisture_queue):
        threading.Thread.__init__(self)
        self.device_number = device_number
        self.access_token = access_token
        self.moisture_queue = moisture_queue
        self.inc = 0 #DELET THIS
        
    def moisture(self):
        print("Getting moisture")
        moisture = get_moisture(self.device_number, self.access_token)
        moisture -= self.inc
        self.inc += 3
        
        #Store the data into a file in date|moisture format
        with open('moisture.data', 'a') as dataf:
            now = datetime.now().isoformat()
            log_string = "%s|%s\n" % (now, moisture)
            dataf.write(log_string)
    
        print("\033[32m->Successfully read moisture\033[39m")
        return moisture

        
        
    def run(self):
        #Loop endlessly
        while True:
            print('-'*10)
            try:
                self.moisture_queue.put(self.moisture())
                sleep(60) #sleep an hour...
            except:
                print("\033[31m->Failed to read moisture. Photon may be offline.")
                sleep(20)
                print("Trying again...")

