from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *
from datetime import datetime, timedelta
from django.db.models import Q
from django.http import HttpResponse,JsonResponse
# Create your views here.

def homepage(request):
    user=tbl_user.objects.get(id=request.session['uid'])
    status=user.user_status
    return render(request, 'User/Homepage.html',{'user':user,'status':status})

def header(request):
    user=tbl_user.objects.get(id=request.session['uid'])
    return render(request, 'User/Header.html', {'user':user})
    
def profile(request):
    user=tbl_user.objects.get(id=request.session['uid'])
    return render(request, 'User/Profile.html', {'user':user})

def edit_profile(request):
    user=tbl_user.objects.get(id=request.session['uid'])
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.phone = request.POST.get('phone')
        user.username = request.POST.get('username')
        if request.FILES.get('user_photo') != None:
            user.user_photo = request.FILES.get('user_photo')
        else:
            user.user_photo = user.user_photo
        user.save()
        return redirect('User:profile')
    return render(request, 'User/EditProfile.html', {'user':user})

def change_password(request):
    user=tbl_user.objects.get(id=request.session['uid'])
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if user.password == old_password:
            if new_password == confirm_password:
                user.password = new_password
                user.save()
                return redirect('User:profile')
            else:
                return render(request, 'User/ChangePassword.html', {'user':user, 'error': 'New password and confirm password do not match'})
        else:
            return render(request, 'User/ChangePassword.html', {'user':user, 'error': 'Old password is incorrect'})
    return render(request, 'User/ChangePassword.html', {'user':user})


def userpreference(request):
    user=tbl_user.objects.get(id=request.session['uid'])
    cuisines=tbl_cuisine.objects.all()
    dishtypes=tbl_dishtype.objects.all()
    if request.method == 'POST':
        cuisine = request.POST.get('cuisine')
        dishtype = request.POST.get('dishtype')
        tbl_userpreference.objects.create(user=user, cuisine_id=cuisine, dish_type_id=dishtype)
        return redirect('User:profile')
    return render(request, 'User/UserPreference.html', {'user':user, 'cuisines':cuisines, 'dishtypes':dishtypes})

def feedback(request):
    user=tbl_user.objects.get(id=request.session['uid'])
    if request.method == 'POST':
        content = request.POST.get('content')
        tbl_feedback.objects.create(user=user, content=content)
        return redirect('User:homepage')
    return render(request, 'User/Feedback.html', {'user':user})

def viewplan(request):
    plan=tbl_plan.objects.all()
    return render(request, 'User/ViewPlan.html', {'plan':plan})

def subscription(request, id):
    user = tbl_user.objects.get(id=request.session['uid'])
    amount=tbl_plan.objects.get(id=id).plan_price
    if request.method == 'POST':
        plan = tbl_plan.objects.get(id=id)
        end_date = datetime.now() + timedelta(days=plan.plan_duration)  # Calculate end date
        tbl_subscription.objects.create(user=user, plan=plan, end_date=end_date)  # Save end date
        user.user_status=1
        user.save()
        return redirect('User:loader')
    else:
        return render(request, 'User/Payment.html', { 'total':amount})

def loader(request):
    return render(request, 'User/Loader.html')

def payment_success(request):
    return render(request, 'User/Payment_suc.html')
def wishlist(request):
    user=tbl_user.objects.get(id=request.session['uid'])
    wishlist=tbl_wishlist.objects.filter(user=user)
    return render(request, 'User/Wishlist.html', {'user':user, 'wishlist':wishlist})

def add_to_wishlist(request, id):
    user=tbl_user.objects.get(id=request.session['uid'])
    dish=tbl_dish.objects.get(id=id)
    tbl_wishlist.objects.create(user=user, dish=dish)
    return redirect('User:wishlist')

def remove_from_wishlist(request, id):
    user=tbl_user.objects.get(id=request.session['uid'])
    wishlist_item=tbl_wishlist.objects.get(id=id)
    wishlist_item.delete()
    return redirect('User:wishlist')

def post(request):
    user=tbl_user.objects.get(id=request.session['uid'])
    if request.method == 'POST':
        post_content = request.POST.get('post_content')
        post_file = request.FILES.get('post_file')
        tbl_post.objects.create(user=user, post_content=post_content, post_file=post_file)
        return redirect('User:homepage')
    return render(request, 'User/Post.html', {'user':user})

def view_post(request):
    user=tbl_user.objects.get(id=request.session['uid'])
    posts=tbl_post.objects.all()
    return render(request, 'User/ViewPost.html', {'user':user, 'posts':posts})

def like_post(request, id):
    user = tbl_user.objects.get(id=request.session['uid'])
    post = tbl_post.objects.get(id=id)
    existing_like = tbl_like.objects.filter(user=user, post=post).first()
    if existing_like:
        existing_like.delete()
    else:
        tbl_like.objects.create(user=user, post=post)
    
    return redirect('User:view_post')

def unlike_post(request, id):
    user=tbl_user.objects.get(id=request.session['uid'])
    post=tbl_post.objects.get(id=id)
    like=tbl_like.objects.get(user=user, post=post)
    like.delete()
    return redirect('User:view_post')

def comment_post(request, id):
    user=tbl_user.objects.get(id=request.session['uid'])
    post=tbl_post.objects.get(id=id)
    if request.method == 'POST':
        comment_content = request.POST.get('comment_content')
        tbl_comment.objects.create(user=user, post=post, comment_content=comment_content)
        return redirect('User:view_post')
    return render(request, 'User/CommentPost.html', {'user':user, 'post':post})

def dish(request):
    dishtypes = tbl_dishtype.objects.all()
    cuisines = tbl_cuisine.objects.all()
    dishes = tbl_dish.objects.filter(user=request.session['uid'])
    if request.method == "POST":
        tbl_dish.objects.create(
            dish_name=request.POST.get('dish_name'),
            dish_description=request.POST.get('dish_description'),
            dish_photo=request.FILES.get('dish_photo'),
            dish_type=tbl_dishtype.objects.get(dishtype_name=request.POST.get('dish_dishtype')),
            cuisine=tbl_cuisine.objects.get(cuisine_name=request.POST.get('dish_cuisine')),
            user=tbl_user.objects.get(id=request.session['uid'])
        )
        return redirect('User:dish')
    else:
        return render(request, 'User/Dish.html', {'dishtypes': dishtypes, 'cuisines': cuisines, 'dishes': dishes})
    
def delete_dish(request, id):
    dish = tbl_dish.objects.get(id=id)
    dish.delete()
    return redirect('User:dish')

def update_dish(request, id):
    dish = tbl_dish.objects.get(id=id)
    dishtypes = tbl_dishtype.objects.all()
    cuisines = tbl_cuisine.objects.all()
    if request.method == "POST":
        dish.dish_name = request.POST.get('dish_name')
        dish.dish_description = request.POST.get('dish_description')
        if request.FILES.get('dish_photo'):
            dish.dish_photo = request.FILES.get('dish_photo')
        else:
            dish.dish_photo = dish.dish_photo
        dish.dish_type = tbl_dishtype.objects.get(dishtype_name=request.POST.get('dish_dishtype'))
        dish.cuisine = tbl_cuisine.objects.get(cuisine_name=request.POST.get('dish_cuisine'))
        dish.save()
        return redirect('User:dish')
    else:
        return render(request, 'User/Dish.html', {'dish': dish, 'dishtypes': dishtypes, 'cuisines': cuisines})
    

def ingredient(request,id):
    ingredients = tbl_ingredients.objects.filter(ingredient_dish__id=id)
    dishes = tbl_dish.objects.get(id=id)
    if request.method == "POST":
        tbl_ingredients.objects.create(
            ingredient_name=request.POST.get('ingredient_name'),
            ingredient_description=request.POST.get('ingredient_description'),
            ingredient_photo=request.FILES.get('ingredient_photo'),
            ingredient_dish=dishes,
            ingredient_qty=request.POST.get('ingredient_qty')
        )
        return redirect('User:ingredient',id)
    else:
        return render(request, 'User/Ingredient.html', {'ingredients': ingredients})
    
def delete_ingredient(request, id):
    ingredient = tbl_ingredients.objects.get(id=id)
    ingredient.delete()
    return redirect('User:ingredient', ingredient.ingredient_dish.id)

def update_ingredient(request, id):
    ingredient = tbl_ingredients.objects.get(id=id)
    if request.method == "POST":
        ingredient.ingredient_name = request.POST.get('ingredient_name')
        ingredient.ingredient_description = request.POST.get('ingredient_description')
        if request.FILES.get('ingredient_photo'):
            ingredient.ingredient_photo = request.FILES.get('ingredient_photo')
        else:
            ingredient.ingredient_photo = ingredient.ingredient_photo
        
        ingredient.ingredient_qty = request.POST.get('ingredient_qty')
        ingredient.save()
        return redirect('User:ingredient', ingredient.ingredient_dish.id)
    else:
        return render(request, 'User/Ingredient.html', {'ingredient': ingredient})
    
def recommendation(request):
    user=tbl_user.objects.get(id=request.session['uid'])
    user_preference = tbl_userpreference.objects.filter(user=user)
    if user_preference.exists():
        cuisine = user_preference.first().cuisine
        dish_type = user_preference.first().dish_type
        recommendations = tbl_dish.objects.filter(cuisine=cuisine, dish_type=dish_type)
    else:
        recommendations = tbl_dish.objects.all()
    return render(request, 'User/Recommendation.html', {'recommendations': recommendations})


def viewdish(request):
    dishes = tbl_dish.objects.all()
    return render(request, 'User/ViewDish.html', { 'dishes':dishes})


def logout(request):
    del request.session['uid']
    return redirect('Guest:index')

def chatpage(request):
    user = tbl_user.objects.get(id=request.session["uid"])
    return render(request, "User/Chat.html", {"user": user})

def ajaxchat(request):
    if request.method == "POST":
        from_user = tbl_user.objects.get(id=request.session["uid"])
        msg = request.POST.get("msg", "")
        file = request.FILES.get("file", None)
        if msg.strip() or file:
            tbl_chat.objects.create(
                chat_content=msg,
                chat_time=datetime.now(),
                user_from=from_user,
                chat_file=file
            )
        return HttpResponse("Message sent")
    return HttpResponse("Invalid request")

def ajaxchatview(request):
    user = tbl_user.objects.get(id=request.session["uid"])
    chat_data = tbl_chat.objects.all().order_by('chat_time')
    return render(request, "User/ChatView.html", {"data": chat_data, "user": user})

def clearchat(request):
    tbl_chat.objects.filter(user_from_id=request.session["uid"]).delete()
    return HttpResponse("Chat Deleted Successfully...")

def rating(request,mid):
    parray=[1,2,3,4,5]
    mid=mid
    
    counts=0
    counts=stardata=tbl_rating.objects.filter(dish=mid).count()
    if counts>0:
        res=0
        stardata=tbl_rating.objects.filter(dish=mid).order_by('-datetime')
        for i in stardata:
            res=res+i.rating_data
        avg=res//counts
        # print(avg)
        return render(request,"User/Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/Rating.html",{'mid':mid})

def ajaxstar(request):
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')
    
    user_review=request.GET.get('user_review')
    pid=request.GET.get('pid')
    # wdata=tbl_booking.objects.get(id=pid)
    tbl_rating.objects.create(user=tbl_user.objects.get(id=request.session['uid']),user_review=user_review,rating_data=rating_data,dish=tbl_dish.objects.get(id=pid))
    stardata=tbl_rating.objects.filter(artist=pid).order_by('-datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})

def starrating(request):
    r_len = 0
    five = four = three = two = one = 0
    # cdata = tbl_booking.objects.get(id=request.GET.get("pdt"))
    rate = tbl_rating.objects.filter(dish=request.GET.get("pdt"))
    ratecount = tbl_rating.objects.filter(dish=request.GET.get("pdt")).count()
    for i in rate:
        if int(i.rating_data) == 5:
            five = five + 1
        elif int(i.rating_data) == 4:
            four = four + 1
        elif int(i.rating_data) == 3:
            three = three + 1
        elif int(i.rating_data) == 2:
            two = two + 1
        elif int(i.rating_data) == 1:
            one = one + 1
        else:
            five = four = three = two = one = 0
        # print(i.rating_data)
        # r_len = r_len + int(i.rating_data)
    # rlen = r_len // 5
    # print(rlen)
    result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":ratecount}
    return JsonResponse(result)
