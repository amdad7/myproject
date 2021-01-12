from django.urls import path

from . import views
app_name='datac'
urlpatterns=[
    path('',views.indexv, name='index'),
    path('login/',views.login,name='login'),
    path('<int:id>/',views.home,name='home'),
    path('<int:id>/logout/',views.logout,name='logout'),
    path('Create_new_user/',views.Create_user,name='Create_user'),
    path('create/',views.create,name='create')
]
