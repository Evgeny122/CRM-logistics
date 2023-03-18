from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.urls import reverse
from .forms import LoginForm, RegisterForm, ProfilesModelForm
from django.contrib.auth.models import User
from django.http import Http404
from .models import UserInformation
import time

def logout_view(request):
    logout(request)
    return redirect('/')

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        user_name = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=user_name, password=password)
        if user:
            login(request, user)
            return redirect('/')
    return render(request, 'profiles/forms.html', {'form':form})

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user_name = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = User.objects.create_user(user_name, email, password, is_staff=False)
        new_obj = UserInformation()
        new_obj.profile = user
        new_obj.save()
        return redirect('/')
    return render(request, 'profiles/forms.html', {'form' : form, 'register' : True})

def detail_user(request, pk):
    try:
        user = User.objects.get(id=pk)
    except User.DoesNotExist:
        raise Http404
    return render(request, 'profiles/detail.html', {'profile' : user})
    

def edit_user(request, pk):
    try:
        user = User.objects.get(id=pk)
        obj = UserInformation.objects.get(profile=user)
    except User.DoesNotExist:
        raise Http404

    if request.method == "POST":
        form = ProfilesModelForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            ed_obj = form.save(commit=False)
            ed_obj.profile = user
            ed_obj.save()
            return redirect(reverse('detail_user', args = {obj.pk}))
    else:
        form = ProfilesModelForm(instance=obj)

    return render(request, 'profiles/edit_user.html', {'form' : form, 'profile' : user})

def list_users(request):
    try:
        obj = UserInformation.objects.all()
    except User.DoesNotExist:
        raise Http404

    sort_obj = sorted(obj, key=lambda single_obj:(
        single_obj.post == 'Стажер',
        single_obj.post == 'Логист',
        single_obj.post == 'Менеджер',
        single_obj.post == 'Руководитель',
    ))

    return render(request, 'profiles/list_users.html', {'sort_obj' : sort_obj})


def status_user(request, pk):
    try:
        user = User.objects.get(id=pk)
        obj = UserInformation.objects.get(profile=user)
    except User.DoesNotExist:
        raise Http404
    if not obj.status:
        obj.status = True
        obj.save()
    elif obj.status:
        obj.status = False
        obj.save()
    return redirect(('/'))
        

        
