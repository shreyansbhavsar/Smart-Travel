from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.log_out, name='log_out'),
    path('profile', views.profile, name='profile'),
    path('pdashboard', views.pdashboard, name='pdashboard'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('g_dashboard', views.g_dashboard, name='g_dashboard'),
    path('photographer', views.photographer, name='photographer'),
    path('guide', views.guide, name='guide'),
    path('viewprofile/order/<int:id>', views.order, name='order'),
    path('viewprofile/<int:id>', views.viewprofile, name='viewprofile'),
    path('page404', views.page404, name='page404'),
    # path('viewprofile/order/orderdone',views.orderdone, name = 'orderdone')
    path('forgotpassword', views.forgotpassword, name='forgotpassword'),
    path('myorders', views.myorders, name='myorders'),
    path('addphoto/<int:id>', views.addphoto, name='addphoto'),
]
