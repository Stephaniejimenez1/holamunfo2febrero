from django.db import models

# Create your models here.
class Post(models.Model):
    Text = models.TextField()

    def __str__(self):
        return self.Text[:50]
    
    