# coding: utf-8


import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restorder.settings")
django.setup()

from django.conf import settings



from order.models import Lamp
from order.models import Hardware

from metro.metro import sendHex, sendHexNoReturn, makeCommand, readCommand
from metro.libmadli import getCommandNumber

def shxNR(arg, serObj):
    hexstr = arg
    #print "Sending: " + hexstr
    return sendHexNoReturn(hexstr, serObj) 
 

def shx(arg, serObj):
    
    hexstr = arg
    #print "Sending: " + hexstr
    return sendHex(hexstr, serObj) 

import serial

def executeCommand(command_string, device_number, memory_range):


    serObj = serial.Serial('/dev/ttyUSB1',
                       baudrate=4800,
                       bytesize=serial.EIGHTBITS,
                       parity=serial.PARITY_NONE,
                       stopbits=serial.STOPBITS_ONE,
                       timeout=1,
                       xonxoff=0,
                       rtscts=0
                       )


    time_debug = False

    #print "METER 0.3.1"
    #print
    #print command_string
    #print "-----------"
    #print "[ LOGS ]"
    #print



    command_number = getCommandNumber(command_string)


    for memory_address in memory_range:
        #print memory_address
        hexstr = makeCommand(command_number,0,device_number,memory_address)
        
        if command_string == "SetAddr" or command_string == "WriteAddr":
            value = shxNR(hexstr,serObj)
        else: 
            value =  shx(hexstr,serObj)
            #print readCommand(value)
            return readCommand(value)
        #print "Getting: " + value
    
        #print value
        #if value:
        #    r_server.set("Warehouse:1:Device:" + str(device_number) + ":"+command_string+":" + str(memory_address), int("0x"+value[3:5],16))



    
def setDim(lamp_number, dim_level):
    executeCommand('On',lamp_number,range(dim_level,dim_level+1))
    executeCommand('On',lamp_number,range(dim_level,dim_level+1))


lamps = Lamp.objects.all()

for lamp in lamps:
  if lamp.change_required:  
    hardware_address = Hardware.objects.get(id=lamp.hardware.address)
    # now set lamp.wanted_l_level to madli adress hardware.address
    setDim(hardware_address, lamp.wanted_l_level)    
    
    lamp.change_required = False
  
  
