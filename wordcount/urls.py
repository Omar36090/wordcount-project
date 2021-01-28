from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('' , views.index , name='index'),
    path('count/' , views.count , name='count'),
    path('about/' , views.about , name='about'),
    path('admin/', admin.site.urls),
]
