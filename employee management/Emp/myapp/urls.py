from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index,name='home'),
    path('view/',views.view,name='view'),
    path('view/<int:emp_id>',views.view,name='view'),
    path('add/',views.add,name='add'),
    path('update/',views.update,name='update'),
    path('delete/',views.delete,name='delete'),
]
