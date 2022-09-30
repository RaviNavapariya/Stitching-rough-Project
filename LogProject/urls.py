from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from log import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.BaseView, name='base'),
    path('home/', views.HomeView, name='home'),
    path('register/', views.UserRegisterView, name='register'),
    path('login/', views.UserLoginView, name='login'),
    path('otp/', views.MobileOTP, name='otp'),
    path('logout/', views.UserLogoutView, name='logout'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)