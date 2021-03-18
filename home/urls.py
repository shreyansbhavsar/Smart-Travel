from django.urls import path
from django.contrib.auth import views as auth_views
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
    path('guide/<int:filter>', views.guide, name='guide'),
    path('photographer/<int:filter>', views.photographer, name='photographer'),
    path('viewprofile/order/<int:id>', views.order, name='order'),
    path('viewprofile/reviews/<int:id>', views.reviews, name='reviews'),
    path('viewprofile/<int:id>', views.viewprofile, name='viewprofile'),
    path('page404', views.page404, name='page404'),
    path('review/<str:email>',views.review,name='review'),
    path('review/<str:email>/<str:rating>',views.review,name='review'),
    # path('viewprofile/order/orderdone',views.orderdone, name = 'orderdone')
    path('forgotpassword', views.forgotpassword, name='forgotpassword'),
    path('myorders', views.myorders, name='myorders'),
    path('addphoto/<int:id>', views.addphoto, name='addphoto'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'),name="password_reset_complete"),
]
