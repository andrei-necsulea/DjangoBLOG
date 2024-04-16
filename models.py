# blog_app/models.py
from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    first_paragraph = models.TextField()

    def __str__(self):
        return self.title
    

class CartiPost(models.Model):
    title = models.CharField(max_length=200)
    #subtitle = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    #first_paragraph = models.TextField(null=True)  # Set a default value

    def __str__(self):
        return self.title    
    

class CatharsisPost(models.Model):
    title = models.CharField(max_length=200)
    #subtitle = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    #first_paragraph = models.TextField(null=True)  # Set a default value

    def __str__(self):
        return self.title        
    
