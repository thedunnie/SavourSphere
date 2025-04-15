from django.db import models
from Guest.models import *

class tbl_admin(models.Model):
    admin_name = models.CharField(max_length=50, unique=True)
    admin_email = models.EmailField(max_length=100, unique=True)
    admin_password = models.CharField(max_length=100)

class tbl_plan(models.Model):
    plan_name = models.CharField(max_length=50, unique=True)
    plan_description = models.TextField(null=True, blank=True)
    plan_price = models.IntegerField()
    plan_duration = models.IntegerField(help_text="Duration in days")


class tbl_dishtype(models.Model):
    dishtype_name = models.CharField(max_length=50, unique=True)


class tbl_cuisine(models.Model):
    cuisine_name = models.CharField(max_length=50, unique=True)

class tbl_dish(models.Model):
    dish_name = models.CharField(max_length=100)
    dish_description = models.TextField(null=True, blank=True)
    dish_photo = models.FileField(upload_to='dishes/', null=True, blank=True)
    cuisine = models.ForeignKey(tbl_cuisine, on_delete=models.CASCADE)
    dish_type = models.ForeignKey(tbl_dishtype, on_delete=models.CASCADE)
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE,null=True, blank=True)
    dish_status=models.IntegerField(default=0)
    dish_date=models.DateField(auto_now_add=True)


class tbl_ingredients(models.Model):
    ingredient_name = models.CharField(max_length=50, )
    ingredient_description = models.TextField(null=True, blank=True)
    ingredient_photo = models.FileField(upload_to='ingredients/', null=True, blank=True)
    ingredient_dish=models.ForeignKey(tbl_dish, on_delete=models.CASCADE,null=True, blank=True)
    ingredient_qty=models.IntegerField(null=True, blank=True)

