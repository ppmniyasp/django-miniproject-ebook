from django.urls import path
from . import views


urlpatterns = [

    path('user-login/',views.loginProfile, name="user-login"),
    path('user-logout/',views.logoutProfile, name="user-logout"),
    path('user-register-page/',views.registerProfile, name="user-register"),

    path('', views.displayBooks, name='user-books'),
    path('user-view-book/<str:pk>', views.viewBook, name='user-view-book'),


    path('user-add-review/<str:pk>', views.addReview, name='user-add-review'),

    path('send_message/<str:pk>', views.send_message, name='send_message'),
    path('message_sent/', views.message_status, name='message_sent'),
    path('user-delete-message/<str:pk>', views.delete_order, name='user-delete-message'),
    

]