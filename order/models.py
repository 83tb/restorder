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
    identifier = models.CharField(max_length= 255, blank = True)
    mpoint = models.PointField()
    group = models.ForeignKey('LGroup', blank=True, null=True )
    objects = models.GeoManager()
        
class LGroup(models.Model):
    identifier = models.CharField(max_length= 255, blank = True)


class Area(models.Model):
    identifier = models.CharField(max_length = 255, blank = True)
    label = models.CharField(max_length = 255, blank = True)
    mpoly = models.MultiPolygonField()
    objects = models.GeoManager()
    level = models.IntegerField(blank=True, null=True)
    
    