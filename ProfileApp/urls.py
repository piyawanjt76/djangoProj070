from django.contrib import admin
from django.urls import path
from ProfileApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home, name='Home'),
    path('History',views.History, name='History'),
    # path('ProfileApp/hny',views.hny, name='hny'),
    path('hny',views.hny,name='hny')
]