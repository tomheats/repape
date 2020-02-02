from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from accounts.forms import EditProfileForm, EditAdditionalInfoForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import PasswordResetView
from accounts.models import UserProfile


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords must match'})

    else:
        return render(request, 'accounts/signup.html')


def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Username or password incorrect.'})

    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home')

    return render(request, 'accounts/signup.html')


def profile(request):
    return render(request, 'accounts/profile.html', {'user': request.user})


def profile_edit(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')

    else:
        form = EditProfileForm(instance=request.user)
        return render(request, 'accounts/edit_profile.html', {'form': form})


def additional_info(request):
    if request.method == "POST":
        form = EditAdditionalInfoForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')

    else:
        form = EditAdditionalInfoForm(instance=request.user.userprofile)
        return render(request, 'accounts/edit_additional_info.html', {'form': form})


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/accounts/profile')
        else:
            return redirect('/accounts/change-password')

    else:
        form = PasswordChangeForm(user=request.user)

        return render(request, 'accounts/change_password.html', {'form': form})
