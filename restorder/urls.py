from django.conf.urls import patterns, url, include
from rest_framework import routers, permissions
from order import views

router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)

router.register(r'ars', views.AreaViewSet)
router.register(r'lamp', views.LampViewSet)
router.register(r'volume', views.VolumeViewSet)
router.register(r'lgroup', views.LGroupViewSet)
router.register(r'hardware', views.HardwareViewSet)

#router.register(r'lamploc', views.LampList.as_view())




from django.contrib import admin
admin.autodiscover()


from rest_framework.urlpatterns import format_suffix_patterns


import settings
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.

urlpatterns = patterns('',

        # unhash this to get access to json user/group api
        #url(r'^meta/', include(router.urls)),
        url(r'^storage/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),

        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        url(r'^admin/', include(admin.site.urls)),        
        
        )


urlpatterns_to_suffix = patterns('',

        url(r'^message/(?P<pk>[0-9]+)/$', views.MsgDetail.as_view()),
        url(r'^messages/', views.MsgList.as_view()),
        url(r'^last/', views.MsgListLast.as_view()),
        url(r'^do/', views.do),
        url(r'^getram/', views.getRamValue),
        url(r'^setdim/', views.setDim),
        url(r'^on/', views.turnOn),
        url(r'^off/', views.turnOff),
        

         url(r'^$', views.MsgList.as_view()),
       
        )
 
 
urlpatterns_suffixed = format_suffix_patterns(urlpatterns_to_suffix)
urlpatterns += router.urls
urlpatterns += urlpatterns_suffixed

