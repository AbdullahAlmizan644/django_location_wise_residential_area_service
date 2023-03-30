from django.urls import path
from .views import index,about,contact,teacher,tution,rent,rent_details


urlpatterns=[
    path("",index,name="index"),
    path("about",about,name="about"),
    path("contact",contact,name="contact"),
    path("teacher",teacher,name="teacher"),
    path("tution",tution,name="tution"),
    path("rent",rent,name="rent"),
    path("rent_details/<int:id>",rent_details,name="rent_details"),


]