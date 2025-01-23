from django.contrib import admin
from django.urls import path
from . import views
from homeapp.views import *
urlpatterns = [
    path('',index,name="index"),
    path('register',register,name="register"),
    path('login_user',login_user,name="login_user"),
    path('registerpage',registerpage,name="registerpage"),
    path('dealer',dealer,name="dealer"),
    path('user',user,name="user"),
    path('loginpage',loginpage, name='loginpage'),
    path('logout/', views.logout_view, name='logout'),
    path('carlist',carlist,name="carlist"),
    path('bikelist',bikelist,name="bikelist"),
    path('aboutus',aboutus,name="aboutus"),
    path('dealercarlist',dealercarlist,name="dealercarlist"),
    path('dealerbikelist',dealerbikelist,name="dealerbikelist"),
    path('dealervehiclelist',dealervehiclelist,name="dealervehiclelist"),
    path('customervehiclelist',customervehiclelist,name="customervehiclelist"),
    path('add_car',add_car,name="add_car"),
    path('add_bike/',add_bike,name="add_bike"),
    path('carrent/<str:id>/',carrent,name="carrent"),
    path('bikerent/<str:id>/',bikerent,name="bikerent"),
    path('payment',payment,name="payment"),
    path('remove_car/<uuid:rent_id>/',remove_car, name='remove_car'),
    path('remove_bike/<uuid:rent_id>/',remove_bike, name='remove_bike'),
    path('update_login',update_login,name="update_login"),
    path('updatepasswordpage',updatepasswordpage,name="updatepasswordpage"),
    
    

    
  
  
    
    
   ]