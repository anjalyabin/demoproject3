from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name='movieapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('movie/<int:id>/',views.detail,name='detail'),
    path('add/',views.add_movie,name='add_movie'),
    path('update/<int:id>/',views.update,name='update'),
path('delete/<int:id>/',views.delete,name='delete')
]
urlpatterns += staticfiles_urlpatterns()