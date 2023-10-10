
from django.urls import path
from . import views

urlpatterns = [
    path('',views.listContacts, name="list-contacts" ),
    path('add_contacts',views.hello, name="add-contacts" ),
    path('update_contact/<str:pk>',views.updateContacts, name="update-contacts" ),
    path('delete_contact/<str:pk>',views.deleteContacts, name="delete-contact" ),
    
]