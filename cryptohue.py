##  Philips Hue Price Tracker  ##
##  Let Crypto Price Control Your lights  ##
__author__      = "Warren Atkins"
__copyright__   = "Copyright 2021, Warren Atkins"


import requests
import os
from qhue import Bridge
import time



found=""
updatetime=5 ## this value changes the time between updates, default set at 15 seconds

def createconfig():
    if os.path.exists("store.txt"):
        print("The config file already exist")
    else:
        print("The config file does not exist")
        print("creating config file")
        f = open("store.txt", "x")
    lines = tuple(open("store.txt", 'r'))
    print(lines)
    if lines == ():
        print("empty")
        addUser()
    else:
        global username
        username=(lines[1])

def getIp():
    findip = requests.get("https://discovery.meethue.com/")
    findip = findip.json()
    global gip
    gip = findip[0]["internalipaddress"]
    print("found the gateway ip "+gip)

def addUser():
    data = {"devicetype":"my_hue_app#cryptolight"}
    r = requests.post("http://" + gip + "/api", json=data)
    adduserresp=r.json()
    print("attempting to bind to hue gateway")

    if "error" in adduserresp[0]:
        print("press button and try again")
        addUser()
    else:
        print("successfully binded to gateway")
        global username
        username=adduserresp[0]["success"]["username"]

def getLight():
    result = requests.get("http://"+gip+"/api/"+username+"/lights")
    result=result.json()
    for i in result:
        if result[i]["state"]["on"] == True:

            found=True
            print(result[i]["name"]+" lamp number "+i+" is turned on")
            global targetlamp
            targetlamp = i
        else:
            found=False
            #print(i+" is turned off")
    if found == False:
        print("no lights found, is the target light turned on?")


def getPrice():
    time.sleep(updatetime)
    result = requests.get("https://api.coinbase.com/v2/prices/ETH-USD/buy")
    arr = result.json()
    ethusd=(arr["data"]["amount"])
    print("$"+ethusd)
    return ethusd

def controlLamp():
    print("getting initial price")
    initial = getPrice()
    print("Initial Price: ${}".format(initial))
    while True:
        current = getPrice()
        if initial == current:
            pass
        else:
            print("Price updated")
            if initial<current:
                print("higher")
                Bridge(gip, username).lights[targetlamp].state(bri=255, hue=23959, sat=254)
            else:
                print("lower")
                Bridge(gip, username).lights[targetlamp].state(bri=255, hue=0, sat=254)
            initial = getPrice()
            pass

def writevals():
    f = open("store.txt", "w")
    f.write(gip + "\n")
    f.write(username)
    f.close()

getIp()
createconfig()
getLight()
writevals()
controlLamp()
