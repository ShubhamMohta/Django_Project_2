from django.urls import path
from . import views
urlpatterns=[

    path("",views.index_mail,name="index_mail"),

]
