from typing import Any
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Books(models.Model):
    LANGUAGE = (
        ('English','English'),
        ('Malayalam','Malayalam'),
        ('Hindi','Hindi'),
        ('Urdu','Urdu'),
        ('Arabic','Arabic'),
        ('Telugu','Telugu'),
        ('Tamil','Tamil'),
        ('Kannada','Kannada'),
        ('Sanskriti','Sanskriti'),     
    )
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=100, null=True, blank=True)
    auther = models.CharField(max_length=100, null=True, blank=True)
    publisher = models.CharField(max_length=100, null=True, blank=True)
    released = models.DateField(null=True, blank=True)
    language = models.CharField(max_length=50, choices=LANGUAGE)
    description = models.TextField(null=True , blank=True)
    auther_description = models.TextField(null=True , blank=True)
    cover_img = models.ImageField(null=True,blank=True)
    types = models.ManyToManyField('Types')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    
    @property
    def imageURL(self):
        try:
            img = self.cover_img.url
        except:
            img = ''
        return img

    class Meta:
        ordering = ['title']

class Review(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100,null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    def __str__(self):
        return self.title
    

class Types(models.Model):
    types = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.types