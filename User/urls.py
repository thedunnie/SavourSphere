from django.urls import path
from User import views

app_name = 'User'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('header/', views.header, name='header'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('userpreference/', views.userpreference, name='userpreference'),
    path('feedback/', views.feedback, name='feedback'),
    path('viewplan/', views.viewplan, name='viewplan'),
    path('subscription/<int:id>/', views.subscription, name='subscription'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/add/<int:id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('post/', views.post, name='post'),
    path('view_post/', views.view_post, name='view_post'),
    path('post/like/<int:id>/', views.like_post, name='like_post'),
    path('post/unlike/<int:id>/', views.unlike_post, name='unlike_post'),
    path('post/comment/<int:id>/', views.comment_post, name='comment_post'),
    path('dish/', views.dish, name='dish'),
    path('dish/delete/<int:id>/', views.delete_dish, name='delete_dish'),
    path('dish/update/<int:id>/', views.update_dish, name='update_dish'),
    path('ingredient/<int:id>/', views.ingredient, name='ingredient'),
    path('ingredient/delete/<int:id>/', views.delete_ingredient, name='delete_ingredient'),
    path('ingredient/update/<int:id>/', views.update_ingredient, name='update_ingredient'),
    path('recommendation/', views.recommendation, name='recommendation'),
    path('logout/', views.logout, name='logout'),
    path('viewdish/', views.viewdish, name='viewdish'),

    path('chatpage/',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),

    path('loader/',views.loader,name="loader"),
    path('payment_success/',views.payment_success,name="payment_success"),
     path('rating/<int:mid>',views.rating,name="rating"),  
    path('ajaxstar/',views.ajaxstar,name="ajaxstar"),
    path('starrating/',views.starrating,name="starrating"),
]   

