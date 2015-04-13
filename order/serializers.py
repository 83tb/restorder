from django.contrib.auth.models import User, Group
from rest_framework import serializers
from order.models import Lamp, Area, LGroup, Volume, Hardware



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

from order.models import Msg

class MsgSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Msg
        fields = ('message_id','timestamp','source','destination','channel','signature','body')


class LGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LGroup

        fields = ('identifier',)

class VolumeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Volume

        fields = ('brightness','volume','group')

from rest_framework_gis import serializers


class AreaSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = Area
        geo_field = "mpoly"
        fields = ('identifier', 'label', 'mpoly', 'level')

class LampSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = Lamp
        geo_field = "geo_position"
        fields = ('identifier', 'geo_position','group','virtual_sensor','hardware','working_l_setting','special_l_setting','presence_l_setting','wanted_l_level','actual_driver_value','presence_flag','special_flag','working_flag','change_required')



    objects = models.GeoManager()


class HardwareSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = Hardware

        fields = ('identifier', 'protocol','building','is_sensor','type','computer_ip')

