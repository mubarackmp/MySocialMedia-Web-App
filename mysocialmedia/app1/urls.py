from django.contrib import admin
from django.urls import path
from app1 import views

app_name = 'app1'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('reels/',views.reels,name='reels'),
    path('signup/',views.usersignup,name='user_signup'),
    path('login/',views.userlogin,name='user_login'),
    path('logout/',views.userlogout,name='user_logout'),
    path('explore/',views.explore,name='explore'),
    path('addpost/',views.addpost,name='addpost'),
    path('addreels/',views.addreels,name='addreels'),
    path('fup/',views.followeduserprofile,name='fup'),
    path('myprofile/',views.myprofile,name='myprofile'),
    path('up/',views.userprofile,name='up'),

]