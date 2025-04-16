from django.urls import path
from Admin import views
app_name = 'Admin'

urlpatterns = [

    path('admin/', views.admin, name='admin'),
    path('home/', views.homepage, name='homepage'),
    path('dishtype/', views.dishtype, name='dishtype'),
    path('delete_dishtype/<int:id>/', views.delete_dishtype, name='delete_dishtype'),
    path('update_dishtype/<int:id>/', views.update_dishtype, name='update_dishtype'),
    path('cuisine/', views.cuisine, name='cuisine'),
    path('delete_cuisine/<int:id>/', views.delete_cuisine, name='delete_cuisine'),
    path('update_cuisine/<int:id>/', views.update_cuisine, name='update_cuisine'),
    path('dish/', views.dish, name='dish'),
    path('delete_dish/<int:id>/', views.delete_dish, name='delete_dish'),
    path('update_dish/<int:id>/', views.update_dish, name='update_dish'),
    path('ingredients/<int:id>', views.ingredient, name='ingredients'),
    path('delete_ingredients/<int:id>/', views.delete_ingredient, name='delete_ingredients'),
    path('update_ingredients/<int:id>/', views.update_ingredient, name='update_ingredients'),
    path('plan/', views.plan, name='plan'),
    path('delete_plan/<int:id>/', views.delete_plan, name='delete_plan'),
    path('update_plan/<int:id>/', views.update_plan, name='update_plan'),
    path('user/', views.users, name='user'),
    path('block_user/<int:id>/', views.blockuser, name='block_user'),
    path('unblock_user/<int:id>/', views.unblockuser, name='unblock_user'),
    path('viewpost/', views.viewpost, name='viewpost'),
    path('block_post/<int:id>/', views.blockpost, name='block_post'),
    path('viewcomplaint/', views.viewcomplaint, name='viewcomplaint'),
    path('reply/<int:id>/', views.reply, name='reply'),
    path('viewdish/', views.viewdish, name='viewdish'),
    path('blockdish/<int:id>/', views.blockdish, name='blockdish'),
    path('unblockdish/<int:id>/', views.unblockdish, name='unblockdish'),

    
    path('chatpage/',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),

    path('logout/', views.logout, name='logout'),

    
    


]
