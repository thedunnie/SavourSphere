from django.db import models
from Admin.models import *
from Guest.models import *
# Create your models here.





class tbl_feedback(models.Model):
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE,)
    content = models.TextField()

class tbl_subscription(models.Model):
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    plan = models.ForeignKey(tbl_plan, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    subscription_status = models.IntegerField(default=0)

class tbl_userpreference(models.Model):
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    cuisine = models.ForeignKey(tbl_cuisine, on_delete=models.CASCADE)
    dish_type = models.ForeignKey(tbl_dishtype, on_delete=models.CASCADE)

class tbl_wishlist(models.Model):
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    dish = models.ForeignKey(tbl_dish, on_delete=models.CASCADE)

class tbl_post(models.Model):
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    post_content = models.TextField()
    post_file = models.FileField(upload_to='posts/', null=True, blank=True)
    post_date=models.DateTimeField(auto_now_add=True)
    post_status=models.IntegerField(default=0)

class tbl_like(models.Model):
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    post = models.ForeignKey(tbl_post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class tbl_comment(models.Model):
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    post = models.ForeignKey(tbl_post, on_delete=models.CASCADE)
    comment_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class tbl_follow(models.Model):
    follower = models.ForeignKey(tbl_user, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(tbl_user, on_delete=models.CASCADE, related_name='followers')
    created_at = models.DateTimeField(auto_now_add=True)



class tbl_complaint(models.Model):

    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    post = models.ForeignKey(tbl_post, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    complaint_status = models.IntegerField(default=0)  
    complaint_reply=models.TextField(null=True, blank=True)
    complaint_date=models.DateTimeField(auto_now_add=True)

class tbl_chat(models.Model):
    chat_content = models.CharField(max_length=500)
    chat_time = models.DateTimeField()
    chat_file = models.FileField(upload_to='ChatFiles/')
    user_from = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_from",null=True, blank=True)

class tbl_rating(models.Model):
    rating_data=models.IntegerField()
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    user_review=models.CharField(max_length=500)
    dish=models.ForeignKey(tbl_dish,on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True)