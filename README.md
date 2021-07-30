# Philips-Crypto-Hue
##  Philips Hue Price Tracker  ##
##  Let Crypto Price Control Your lights  ##
__author__      = "Warren Atkins"
__copyright__   = "Copyright 2021, Warren Atkins"

Run the EXE file or directly via cryptohue.py
First time running the script the program will find the ip address of your local Philips Hue gateway
It will then ask you to press the bind button on the Hue Gateway
!! Make sure all lights are turned off other than the light you wish to be controlled !!
It will establish Auth and create a new username to allow the program to send commands to the hue devices
Every 10 seconds the price data will be updated and the result will be pushed to the Selected Hue light

First time running the Exe or cryptohue.py will create an additional file store.txt
This file contains the local gateway ip address and the created username, this is to prevent unnessary tasks being run twice.
