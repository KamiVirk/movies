from django.views.generic import ListView, DetailView, DeleteView
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterationForm, ProfileUdateform, UserUpdateForm, AdminRegisterationForm, AdminUpdateForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from base.decorators import staff_required
from django.utils.decorators import method_decorator


def register(request):
    if request.method == 'POST':
        if request.user.is_superuser == True:
            form = AdminRegisterationForm(request.POST)
        else:     
            form = UserRegisterationForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('movie-list')
    else:
        if request.user.is_superuser == True:
            form = AdminRegisterationForm()
        else:
            form = UserRegisterationForm() 
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        if request.user.is_superuser:        
            p_form = ProfileUdateform(request.POST, request.FILES, instance=request.user.profile)
            u_form = AdminUpdateForm(request.POST, instance=request.user)
        else:
            p_form = ProfileUdateform(request.POST, request.FILES, instance=request.user.profile)
            u_form = UserUpdateForm(request.POST, instance=request.user)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account is updated')
            return redirect('profile')
    else:
        if request.user.is_superuser == True:
            p_form = ProfileUdateform(instance=request.user.profile)
            u_form = AdminUpdateForm(instance=request.user)
        else:
            p_form = ProfileUdateform(instance=request.user.profile)
            u_form = UserUpdateForm(instance=request.user)

    context = {'p_form': p_form, 'u_form': u_form}
    return render(request, 'users/profile.html', context)


@method_decorator(staff_required, name='dispatch')
class UserSettings(ListView):
    model = User
    template_name = 'users/user_settings.html'
    context_object_name = 'user_s'
      
@method_decorator(staff_required, name='dispatch')
class UserDetails(DetailView):
    model = User
    template_name = 'users/user_details.html'
    context_object_name = 'users'

@method_decorator(staff_required, name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    template_name = 'users/user_confirm_delete.html' 

    success_url = '/users/'