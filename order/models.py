from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User, Group

import uuid # from http://zesty.ca/python/uuid.html
import sys
import base64 

from django.contrib.gis.db import models
 
 
def fetch_code(custom_string="CODE_"):
    """
    usage:
    fetch_code()   
    fetch_code(custom_string="KEY_")
  
    """
    b64uid = '00000000'
    
   
    uid = uuid.uuid4()
    b64uid = base64.b64encode(uid.bytes,'-_')
    
    code = b64uid[0:6]



    return custom_string+code





def validate_file(fieldfile_obj):
    """
    Validation of size
    """
    filesize = fieldfile_obj.file.size
    kilobyte_limit = 65
    if filesize > kilobyte_limit*1024:
        raise ValidationError("Max file size is %skB" % str(kilobyte_limit))

# Create your models here.
class Msg( models.Model ):
    """
    Model for storing `messages`
    """

    def validate_file(fieldfile_obj):
        """
        Validation of size
        """
        filesize = fieldfile_obj.file.size
        kilobyte_limit = 65
        if filesize > kilobyte_limit*1024:
            raise ValidationError("Max file size is %skB" % str(kilobyte_limit))

    message_id = models.CharField( max_length = 255, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    source = models.CharField( max_length = 255 )
    destination = models.CharField( max_length = 255 )
    channel = models.CharField( max_length = 255 )
    signature = models.CharField( max_length = 255 )
    body = models.FileField(upload_to="messages/%Y/%m/%d/", validators=[validate_file],blank=True)

    def save(self, *args, **kwargs):
        self.message_id = fetch_code(custom_string="0_")
        super(Msg, self).save(*args, **kwargs)



class Volume(models.Model):
    brightness = models.IntegerField()
    volume = models.IntegerField()
    group = models.ForeignKey('LGroup', blank=True, null=True)


class Lamp(models.Model):

    def recount(self):
        if self.special_flag:
            #self.actual_driver_value = self.special_l_setting
            print self.special_l_setting
            #self.wanted_l_level = 0 #self.special_l_setting
            #self.change_required = True
        #self.save()



    identifier = models.CharField(max_length= 255, blank = True)

    ## New definition of Lamp

    virtual_sensor = models.ForeignKey('VirtualSensor', blank=True, null=True)
    # may contain a mistake
    group = models.ManyToManyField('LGroup', blank=True, null=True )
    geo_position = models.PointField()
    hardware = models.ForeignKey('Hardware', blank=True, null=True)

    # semi-static
    working_l_setting = models.IntegerField()
    special_l_setting = models.IntegerField()
    presence_l_setting = models.IntegerField()

    # dynamic

    wanted_l_level = models.IntegerField()
    actual_driver_value = models.IntegerField()

    presence_flag = models.BooleanField(default=False)
    special_flag = models.BooleanField(default=False)
    working_flag = models.BooleanField(default=False)

    change_required = models.BooleanField(default=False)


    ## deleted
    mpoint = models.PointField()

    objects = models.GeoManager()
        
class LGroup(models.Model):
    identifier = models.CharField(max_length= 255, blank = True)
    madli_group = models.IntegerField()
    has_madli = models.BooleanField(default=False)


class Area(models.Model):
    identifier = models.CharField(max_length = 255, blank = True)
    label = models.CharField(max_length = 255, blank = True)
    mpoly = models.MultiPolygonField()
    objects = models.GeoManager()
    level = models.IntegerField(blank=True, null=True)
    

class Hardware(models.Model):
    identifier = models.CharField(max_length= 255, blank = True)
    protocol = models.CharField(max_length= 255, blank = True)
    building = models.CharField(max_length= 255, blank = True)
    is_sensor = models.BooleanField(default=False)
    type = models.CharField(max_length= 255, blank = True)
    computer_ip = models.CharField(max_length= 255, blank = True)
    address = models.CharField(max_length= 255, blank = True)


class Building(models.Model):
    identifier = models.CharField(max_length= 255, blank = True)
    label = models.CharField(max_length = 255, blank = True)


class Sensor(models.Model):
    identifier = models.CharField(max_length= 255, blank = True)
    hardware = models.ForeignKey('Hardware', blank=True, null=True)
    value = models.CharField(max_length= 255, blank = True)


class VirtualSensor(models.Model):
    identifier = models.CharField(max_length= 255, blank = True)
    formula = models.CharField(max_length= 255, blank = True)



