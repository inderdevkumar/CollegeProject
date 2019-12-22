from django.db import models

# Create your models here.

class colleges(models.Model):
    name= models.CharField(max_length=200)
    university= models.CharField(max_length=200)
    state= models.CharField(max_length=200)
    location= models.CharField(max_length=200)
    fee= models.PositiveIntegerField()
    grade= models.CharField(max_length=200)
    branch= models.CharField(max_length=200)
    types= models.CharField(max_length=200)
    placed= models.PositiveIntegerField()
    image= models.ImageField(upload_to='images/')
    review= models.CharField(max_length=200)

    def __str__(self):  # This is used to display name as title in admin page  without this it will be looking like : Blog object (4)
        return self.name