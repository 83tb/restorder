from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from order.serializers import UserSerializer, GroupSerializer, VolumeSerializer, LGroupSerializer
from order.models import Msg
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from order.models import Lamp, Area, Volume, LGroup, Hardware
from order.serializers import AreaSerializer, LampSerializer, HardwareSerializer
from rest_framework.renderers import JSONRenderer, YAMLRenderer



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class AreaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
#    renderer_classes = (JSONRenderer, YAMLRenderer)


class LampViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Lamp.objects.all()
    serializer_class = LampSerializer
#    renderer_classes = (JSONRenderer, YAMLRenderer)


class HardwareViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Hardware.objects.all()
    serializer_class = HardwareSerializer
#    renderer_classes = (JSONRenderer, YAMLRenderer)







class LGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = LGroup.objects.all()
    serializer_class = LGroupSerializer
#    renderer_classes = (JSONRenderer, YAMLRenderer)

class VolumeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer





from order.models import Msg
from order.serializers import MsgSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, renderers
from rest_framework.decorators import api_view

from rest_framework import generics
from datetime import datetime, timedelta

class MsgList(generics.ListCreateAPIView):
    queryset = Msg.objects.all().order_by('-timestamp')
    serializer_class = MsgSerializer
    paginate_by = 10
    paginate_by_param = 'page_size'
    max_paginate_by = 100




class MsgListLast(generics.ListCreateAPIView):
    backtime = datetime.now()-timedelta(minutes=10)
    now = datetime.now()+timedelta(minutes=2)
    
    queryset = Msg.objects.filter(timestamp__range=[backtime,now])
    serializer_class = MsgSerializer

    """
    paginate_by = 10
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    """

# here you could easily disconnect Update/Destroy functionality
class MsgDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Msg.objects.all()
    serializer_class = MsgSerializer
    
    
from metro.metro import sendHex, sendHexNoReturn, makeCommand, readCommand

from metro.libmadli import getCommandNumber

from time import time

from rest_framework_gis.filters import InBBoxFilter

import models, serializers

class LampList(ListAPIView):

    queryset = models.Lamp.objects.all()
    serializer_class = serializers.LampSerializer
    bbox_filter_field = 'point'
    filter_backends = (InBBoxFilter, )
    bbox_filter_include_overlapping = True # Optional


def shxNR(arg, serObj):
    hexstr = arg
    #print "Sending: " + hexstr
    return sendHexNoReturn(hexstr, serObj) 
 

def shx(arg, serObj):
    
    hexstr = arg
    #print "Sending: " + hexstr
    return sendHex(hexstr, serObj) 


def executeCommand(command_string, device_number, memory_range):

    import serial

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
    t0 = time()



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


    t1 = time()
    if time_debug: print '[ Sending command took %f sec ]' %(t1-t0)

    t2 = time()
    if time_debug: print '[ Getting response took %f sec ]' %(t2-t1)



def do(request, template="action.html"):
    """
    Show a warehouse.
    """
    
    context = {"warehouse": 1}


    #command_string = 'On'
    #device_number = 195
    #memory_range = range(0,1)

    command_string = request.GET['command']
    device_number = request.GET['device']
    memory_range = range(int(request.GET['start']),int(request.GET['end']))

    output = executeCommand(command_string,device_number,memory_range)
    #job = kolejka.enqueue(executeCommand, command_string,device_number,memory_range)

    
    context = {"output": output}
    return render(request, template, context)


def turnOn(request, template="action.html"):
    lamp_number = request.GET['lamp_number']
    executeCommand('On',lamp_number,range(0,1))
    output = executeCommand('On',lamp_number,range(0,1))
    context = {"output": output}
    return render(request, template, context)

def turnOff(request, template="action.html"):
    lamp_number = request.GET['lamp_number']
    executeCommand('Off',lamp_number,range(0,1))
    output = executeCommand('Off',lamp_number,range(0,1))
    context = {"output": output}
    return render(request, template, context)
    
def setDim(request, template="action.html"):
    lamp_number = int(request.GET['lamp_number'])

    dim_level = int(request.GET['dim_level'])
    
    executeCommand('On',lamp_number,range(dim_level,dim_level+1))
    executeCommand('On',lamp_number,range(dim_level,dim_level+1))

    context = {"output": "Dim does not do output"}
    return render(request, template, context)
    
def getRamValue(request, template="action.html"):

    lamp_number = int(request.GET['lamp_number'])
    address = int(request.GET['address'])
    output = executeCommand('GetRam',lamp_number,range(address,address+1))
    context = {"output": output}
    return render(request, template, context)


"""
lamp_num = 464

turnOn(lamp_num)
setDim(lamp_num, 0, 83)
getRamValue(lamp_num,0)


sleep(1)

turnOn(lamp_num)
setDim(lamp_num, 0, 44)
getRamValue(lamp_num,0)

sleep(1)

turnOff(lamp_num)
setDim(lamp_num, 0, 254)
getRamValue(lamp_num,0)
"""


#sleep(10)

#setDim(lamp_num, 0, 82)
#getRamValue(lamp_num,0)

