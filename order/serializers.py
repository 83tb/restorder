from django.contrib.auth.models import User, Group
from rest_framework import serializers
from order.models import Lamp, Area, LGroup, Volume


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



from rest_framework_gis import serializers


class AreaSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = Area
        geo_field = "mpoly"
        fields = ('identifier', 'label', 'mpoly', 'level')

class LampSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = Lamp
        geo_field = "mpoint"
        fields = ('identifier', 'mpoint','group')

class LGroupSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = LGroup

        fields = ('identifier')

class VolumeSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = Volume

        fields = ('brightness','volume','group')
