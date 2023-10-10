from django.db import models
from django.contrib.auth.models import User
from booksdata.models import Books

# Create your models here.

class UserOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    book_name = models.CharField(max_length=255,null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.user.username} regarding book '{self.book_name}'"
    
    ordering = ['datetime']
