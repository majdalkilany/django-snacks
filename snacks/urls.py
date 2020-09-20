from .views import HomeVew , AboutVew
from django.urls import path


urlpatterns = [
path('',HomeVew.as_view(),name = 'home'),
path('about', AboutVew.as_view(),name = 'about'),

]