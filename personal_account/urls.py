from django.contrib.auth.views import LogoutView
from django.urls import path

from personal_account import views


urlpatterns = [
    path('account', views.Accounts.as_view(), name='acc'),
    path('login', views.log, name='login'),
    path('auth', views.autorize, name='auth'),
    path('logus', views.login_user, name='logus'),
    path('register', views.register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('personalaccount/', views.personal_account, name='personalaccount'),
    path('personalaccount1/', views.personal_account1, name='personalaccount1'),
    path('customers/', views.customers, name='customers'),
    path('executor/', views.executor, name='executor'),
    path('comment/', views.comment, name='comment'),

]