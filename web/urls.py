from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


app_name = 'web'

urlpatterns = [
    path('', login, name='login'),
    path('main1/', main1, name='main1'),
    path('button02/', button02, name='button02'),
    path('button01_true/', button01_true, name='button01_true'),
    path('logout/', logout, name='logout'),
    path('howuse/', how_use, name='how_use'),

]