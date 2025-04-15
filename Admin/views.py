from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *
# Create your views here.

def homepage(request):
    return render(request, 'Admin/Homepage.html')

def logout(request):
    del request.session['aid']
    return redirect('Guest:login')

def admin(request):
    if request.method == "POST":
        tbl_admin.objects.create(
            admin_name=request.POST.get('admin_name'),
            admin_email=request.POST.get('admin_email'),
            admin_password=request.POST.get('admin_password')
        )
        return redirect('Admin:admin')
    else:
        return render(request, 'Admin/AdminReg.html')
    

def dishtype(request):
    dishtypes = tbl_dishtype.objects.all()
    if request.method == "POST":
        tbl_dishtype.objects.create(
            dishtype_name=request.POST.get('dishtype_name')
        )
        return redirect('Admin:dishtype')
    else:
        return render(request, 'Admin/Dishtype.html', {'dishtypes': dishtypes})
    
def delete_dishtype(request, id):
    dishtype = tbl_dishtype.objects.get(id=id)
    dishtype.delete()
    return redirect('Admin:dishtype')

def update_dishtype(request, id):
    dishtype = tbl_dishtype.objects.get(id=id)
    if request.method == "POST":
        dishtype.dishtype_name = request.POST.get('dishtype_name')
        dishtype.save()
        return redirect('Admin:dishtype')
    else:
        return render(request, 'Admin/Dishtype.html', {'dishtype': dishtype})
    
def cuisine(request):
    cuisines = tbl_cuisine.objects.all()
    if request.method == "POST":
        tbl_cuisine.objects.create(
            cuisine_name=request.POST.get('cuisine_name')
        )
        return redirect('Admin:cuisine')
    else:
        return render(request, 'Admin/Cuisine.html', {'cuisines': cuisines})
    

def delete_cuisine(request, id):
    cuisine = tbl_cuisine.objects.get(id=id)
    cuisine.delete()
    return redirect('Admin:cuisine')

def update_cuisine(request, id):
    cuisine = tbl_cuisine.objects.get(id=id)
    if request.method == "POST":
        cuisine.cuisine_name = request.POST.get('cuisine_name')
        cuisine.save()
        return redirect('Admin:cuisine')
    else:
        return render(request, 'Admin/Cuisine.html', {'cuisine': cuisine})
    

def dish(request):
    dishtypes = tbl_dishtype.objects.all()
    cuisines = tbl_cuisine.objects.all()
    dishes = tbl_dish.objects.filter(user__isnull=True)
    if request.method == "POST":
        tbl_dish.objects.create(
            dish_name=request.POST.get('dish_name'),
            dish_description=request.POST.get('dish_description'),
            dish_photo=request.FILES.get('dish_photo'),
            dish_type=tbl_dishtype.objects.get(dishtype_name=request.POST.get('dish_dishtype')),
            cuisine=tbl_cuisine.objects.get(cuisine_name=request.POST.get('dish_cuisine'))
        )
        return redirect('Admin:dish')
    else:
        return render(request, 'Admin/Dish.html', {'dishtypes': dishtypes, 'cuisines': cuisines, 'dishes': dishes})
    
def delete_dish(request, id):
    dish = tbl_dish.objects.get(id=id)
    dish.delete()
    return redirect('Admin:dish')

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
        return redirect('Admin:dish')
    else:
        return render(request, 'Admin/Dish.html', {'dish': dish, 'dishtypes': dishtypes, 'cuisines': cuisines})
    

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
        return redirect('Admin:ingredients',id)
    else:
        return render(request, 'Admin/Ingredient.html', {'ingredients': ingredients})
    
def delete_ingredient(request, id):
    ingredient = tbl_ingredients.objects.get(id=id)
    ingredient.delete()
    return redirect('Admin:ingredient', ingredient.ingredient_dish.id)

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
        return redirect('Admin:ingredient', ingredient.ingredient_dish.id)
    else:
        return render(request, 'Admin/Ingredient.html', {'ingredient': ingredient})
    

def plan(request):
    plans = tbl_plan.objects.all()
    if request.method == "POST":
        tbl_plan.objects.create(
            plan_name=request.POST.get('plan_name'),
            plan_price=request.POST.get('plan_price'),
            plan_duration=request.POST.get('plan_duration'),
            plan_description=request.POST.get('plan_description')
        )
        return redirect('Admin:plan')
    else:
        return render(request, 'Admin/Plan.html', {'plans': plans})
    
def delete_plan(request, id):
    plan = tbl_plan.objects.get(id=id)
    plan.delete()
    return redirect('Admin:plan')

def update_plan(request, id):
    plan = tbl_plan.objects.get(id=id)
    if request.method == "POST":
        plan.plan_name = request.POST.get('plan_name')
        plan.plan_price = request.POST.get('plan_price')
        plan.plan_duration = request.POST.get('plan_duration')
        plan.plan_description = request.POST.get('plan_description')
        plan.save()
        return redirect('Admin:plan')
    else:
        return render(request, 'Admin/Plan.html', {'plan': plan})
    
def viewcomplaint(request):
    complaints = tbl_complaint.objects.filter(complaint_status=0)
    replied= tbl_complaint.objects.filter(complaint_status=1)
    return render(request, 'Admin/ViewComplaint.html', {'complaints': complaints, 'replied':replied})

def reply(request,id):
    complaint = tbl_complaint.objects.get(id=id)
    if request.method == "POST":
        complaint.complaint_reply=request.POST.get('complaint_reply')
        complaint.complaint_status=1
        complaint.save()
        return redirect('Admin:viewcomplaint')
    else:
        return render(request, 'Admin/Reply.html', {'complaint': complaint})
    

def users(request):
    users = tbl_user.objects.all()
    return render(request, 'Admin/Users.html', {'users': users})

def blockuser(request, id):
    user = tbl_user.objects.get(id=id)
    user.user_status=2
    user.save()
    return redirect('Admin:users')

def unblockuser(request, id):
    user = tbl_user.objects.get(id=id)
    user.user_status=0
    user.save()
    return redirect('Admin:users')

def viewpost(request):
    posts = tbl_post.objects.all()
    return render(request, 'Admin/ViewPost.html', {'posts': posts})

def blockpost(request, id):
    post = tbl_post.objects.get(id=id)
    post.post_status=1
    post.save()
    return redirect('Admin:viewpost')

def unblockpost(request, id):
    post = tbl_post.objects.get(id=id)
    post.post_status=0
    post.save()
    return redirect('Admin:viewpost')

def viewdish(request):
    dishes = tbl_dish.objects.filter(user__isnull=False)
    return render(request, 'Admin/ViewDish.html', {'dishes': dishes})


def blockdish(request, id):
    dish = tbl_dish.objects.get(id=id)
    dish.dish_status=1
    dish.save()
    return redirect('Admin:viewdish')

def unblockdish(request, id):
    dish = tbl_dish.objects.get(id=id)
    dish.dish_status=0
    dish.save()
    return redirect('Admin:viewdish')