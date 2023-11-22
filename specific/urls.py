from specific.views import *
from django.urls import path
app_name='BGMI'
urlpatterns=[
    path('soulsai/',soulsai,name='soulsai'),
    path('soulvigi/',soulvigi,name='soulvigi'),
]