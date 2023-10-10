from django.urls import path
from . import views


urlpatterns = [

    path('login/',views.loginProfile, name="login"),
    path('logout/',views.logoutProfile, name="logout"),
    path('register-page/',views.registerProfile, name="register"),

    path('admin_messages/', views.admin_messages, name='admin_messages'),
    path('approve_message/<int:message_id>/', views.approve_message, name='approve_message'),
    path('reject_message/<int:message_id>/', views.reject_message, name='reject_message'),
    path('delete_message/<int:message_id>/', views.delete_message, name='delete_message'),

    path('', views.displayBooks, name='books'),
    path('add-book/', views.addBook, name='add-books'),
    path('view-book/<str:pk>', views.viewBook, name='view-book'),
    path('edit-book/<str:pk>', views.editBook, name='edit-book'),
    path('delete-book/<str:pk>', views.deleteBook, name='delete-book'),


    path('add-review/<str:pk>', views.addReview, name='add-review'),
    path('edit-review/<str:pk>/<str:review_id>', views.editReview, name='edit-review'),
    path('delete-review/<str:pk>/<str:review_id>', views.deleteReview, name='delete-review'),

]