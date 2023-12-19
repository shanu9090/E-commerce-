from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import MyPasswordChange

urlpatterns = [
    path("signup/",views.sign_up, name='signup'),
    path("login/",views.log_in, name='login'),
    path("logout/",views.log_out, name='logout'),

    # path('adminreg/', views.adminreg,name="signup"),
    # path('admininsert/',views.adminreginsert,name="adminreginsert"),
    # path('adminlogin/',views.adminlogin,name="login"),


    path('passwordchange/',auth_views.PasswordChangeView.as_view
        (template_name='auth1/passwordchange.html',form_class=MyPasswordChange,
         success_url='/passwordchangedone/'), name="passwordchange"),
         
    path('passwordchangedone/',auth_views.PasswordChangeView.as_view
         (template_name="auth1/passwordchangedone.html"),name='passwordchangedone')    

]