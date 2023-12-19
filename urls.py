from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('woman/',views.woman_clothes,name="woman"),
    path('man/',views.man_clothes,name="man"),
    path('kids/',views.kids_clothes,name="kids"),

    path('mycart/',views.mycart,name="mycart"),
    path('search/',views.search,name="search"),
    path('payment/',views.make_payment,name="payment"),
    path('mycart/',views.mycart_search,name="mycart1"),
    path('profile/',views.ProfileView.as_view(),name="profile"),
     path('userprofile/',views.userprofile,name="userprofile"),
    path('myorder/',views.order,name="order"),
    path('addresscrud/<int:id>/',views.addresscrud,name="addresscrud"),
    path('addresscrudupdate/<int:id>/',views.addresscrudupdate,name="addresscrudupdate"),


    path('address/',views.address,name="address"),
    path('checkout/',views.checkout,name="checkout"),

    path('payment/',views.make_payment,name="payment"),
    path('paymentdone/',views.paymentdone,name="paymentdone"),
    path('item_payment/',views.item_payment,name='item_payment'),
    path('payment-Status/',views.payment_status,name='payment-status')






   # path('changepassword/',views.changepassword,name="changepassword"),
   # path('profile/',views.profile,name="profile"),
] 
