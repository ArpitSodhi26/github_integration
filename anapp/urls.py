from django.urls import path
from django import urls
from django.conf.urls import url
from . import views
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from django.urls import include, path
from django.views.generic.base import TemplateView

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)

# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]


urlpatterns = [
     path('accounts/', include('django.contrib.auth.urls')),
     path('', TemplateView.as_view(template_name = 'home.html'), name = 'home'),
    #  path('', views.get_data, name = 'home'),
     path('social-auth/', include('social_django.urls', namespace='social')),
     path('get_data/', views.get_ddata, name = 'home'),
     

]