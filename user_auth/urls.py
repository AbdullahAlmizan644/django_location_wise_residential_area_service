from django.urls import path
from .views import user_login,user_signup,user_dashboard,user_logout

urlpatterns=[
    path("",user_login,name="user_login"),
    path("user_signup",user_signup,name="user_signup"),
    path("user_dashboard",user_dashboard,name="user_dashboard"),
    path("user_logout",user_logout,name="user_logout"),
]