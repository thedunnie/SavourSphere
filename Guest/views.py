from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'Guest/index.html')

def user(request):
    if request.method == 'POST':
        tbl_user.objects.create(
            username=request.POST.get('username'),
            user_password=request.POST.get('password'),
            user_email=request.POST.get('email'),
            user_phone=request.POST.get('phone'),
            user_first_name=request.POST.get('first_name'),
            user_last_name=request.POST.get('last_name'),
            user_photo=request.FILES.get('user_photo'),
        )
        return redirect('Guest:login')
    else:
        return render(request, 'Guest/User.html')
    
def login(request):
    if request.method == 'POST':
        identifier = request.POST.get('username') 
        password = request.POST.get('password')
        usercount = tbl_user.objects.filter(
            (Q(username=identifier) | Q(user_email=identifier)) & Q(user_password=password)
        ).count()
        admincount = tbl_admin.objects.filter(admin_email=identifier,admin_password=password).count()
        if usercount > 0:
            user=tbl_user.objects.get(
                (Q(username=identifier) | Q(user_email=identifier)) & Q(user_password=password)
            )
            request.session['uid'] = user.id
            return redirect('User:homepage')
        elif admincount > 0:
            admin=tbl_admin.objects.get(admin_email=identifier,admin_password=password)
            request.session['aid'] = admin.id
            return redirect('Admin:homepage')
        else:
            return render(request, 'Guest/Login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'Guest/Login.html')