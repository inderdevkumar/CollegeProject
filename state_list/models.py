from django.db import models

# Create your models here.

class states(models.Model):
    name= models.CharField(max_length=200)

    def __str__(self):
         # This is used to display name as title in admin page  without this it will be looking like : Model_name object (4)
        return self.name

