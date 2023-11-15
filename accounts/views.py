# from django.shortcuts import render
from django.shortcuts import render, redirect 
from django.contrib.auth import  login, logout,authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from accounts.forms import SignUpForm 
from accounts.sendgmail import send_forget_password_mail
from accounts.models import *

# Create your views here.


import uuid
def forget_password_view(request):
    if not request.user.is_authenticated:
        try:
            if request.method == 'POST':
                username1 = request.POST.get('username')
                user = User.objects.filter(username=username1).first()
                user1 = User.objects.filter(email=username1).first()
                if user is None and user1 is None:
                    messages.warning(request, "User doesn't exist!")
                    return redirect('/forget-password')
                elif user != None:
                    user_obj = User.objects.get(username= username1)
                    print(user_obj)
                    token = str(uuid.uuid4())
                    profile_obj = Profile(user=user_obj , forget_password_token = token)
                    profile_obj.save()
                    send_forget_password_mail(user_obj.email, token)
                    messages.add_message(request, messages.SUCCESS, "An email is sent.")

                elif user1 != None:
                    user_obj = User.objects.get(email= username1)
                    token = str(uuid.uuid4())
                    profile_obj = Profile(user=user_obj , forget_password_token = token)
                    profile_obj.save()
                    send_forget_password_mail(user_obj.email, token)
                    messages.add_message(request, messages.SUCCESS, "An email is sent.")
        except Exception as e:
            print(e)   
    return render(request, 'account/forget-password.html')


def reset_password_view(request, token):
    try:
        profile_obj = Profile.objects.filter(forget_password_token = token).first()
        if request.method == 'POST':
            new_password = request.POST.get('password1')
            confirm_password = request.POST.get('password2')
            user_id = request.POST.get('user_id')
            if user_id is None:
                messages.warning(request, "No user id found!")
                return redirect(f'/reset-password/{token}/')
            if new_password != confirm_password:
                messages.warning(request, "please confirm your password correctly.")
                return redirect(f'/reset-password/{token}/')
            user_obj = User.objects.get(id = user_id)
            user_obj.set_password(new_password)
            print(type(user_obj), user_obj, new_password)
            user_obj.save()
            return redirect('account:login')
        
    except Exception as e:
        print(e)
    context = {'user_id': profile_obj.user_id, 'token': token}
    return render(request, 'account/reset-password.html', context)
