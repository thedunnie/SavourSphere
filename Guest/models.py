from django.db import models

# Create your models here.
class tbl_user(models.Model):
    username = models.CharField(max_length=150, unique=True)
    user_first_name = models.CharField(max_length=150)
    user_last_name = models.CharField(max_length=150)
    user_phone = models.CharField(max_length=15)
    user_email = models.EmailField()
    user_password = models.CharField(max_length=128, null=True, blank=True)
    user_status=models.IntegerField(default=0) 
    user_photo=models.FileField(upload_to='user_photos/', null=True, blank=True)

