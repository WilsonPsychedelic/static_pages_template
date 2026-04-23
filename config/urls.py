from django.contrib import admin
from django.urls import path, include
from stat_pgs_tmpl import views
from accounts import views as account_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('page1/', views.p1, name="page1"),
    path('page2/', views.p2, name="page2"),
    path('logout/', account_views.manual_logout, name='logout'),
    path('register/', account_views.register_view, name='register'),
    path('login/', account_views.login_view, name='login'),
    path('accounts/', include('accounts.urls')),
    #path('dashboard/', account_views.dashboard_view, name='dashboard'),
]