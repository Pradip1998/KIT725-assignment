
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.name, name='name'),
    path('register', views.register, name='register'),
    path('customer', views.dashboard, name='dashboard'),
    path('exit', views.exit, name='exit'),
    path('product', views.product, name='product'),
    path('shop', views.shop, name='shop'),
    path('insecure', views.insecure, name='insecure'),
    path('verify', views.verifyotp, name='verify'),
    path('reset_password', login_required(auth_views.PasswordResetView.as_view()), name='reset_password'),
    path('reset_password_sent',login_required(auth_views.PasswordResetDoneView.as_view()), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', login_required(auth_views.PasswordResetConfirmView.as_view()), name='password_reset_confirm'),
    path('reset_password_complete', login_required(auth_views.PasswordResetCompleteView.as_view()), name='password_reset_complete'),


]
