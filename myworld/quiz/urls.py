from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('members/', views.members, name='members'),
    path('members/add/', views.add, name='add'),
    path('members/add/addrecord/', views.addrecord, name='addrecord'),
    path('members/delete/<int:id>', views.delete, name='delete'),
    path('members/update/<int:id>', views.update, name='update'),
    path('members/update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
]