import requests
import urllib.request
import json

device_number = "370048001851373237343331"
access_token = "d3d7d4d4fd0128ca685d0937bfaab00b1a6a0fc7"

def water_plant(device_number, access_token, command):
    params = {'access_token':access_token, 'arg':command}

    url = "https://api.particle.io/v1/devices/%s/waterPlant" % (device_number)

    request = requests.post(url, params)
    data = request.json()

    return data

def ping_particle(device_number, access_token):
    url = "https://api.particle.io/v1/devices/%s/ping?access_token=%s" % (device_number, access_token)
    
    request = requests.put(url)
    data = request.json()

    if data['ok'] == False:
        raise exception("!!!ERROR: Ping was not ok")
    result = data['online']

    return result
    
def get_moisture(device_number, access_token):
# API url stuff
    url = "https://api.particle.io/v1/devices/%s/moisture?access_token=%s" % (device_number, access_token) 

    # Send a GET request
    request = requests.get(url)
    data = request.json()
    moisture = data['result']
    
    return moisture
