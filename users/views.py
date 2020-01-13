from django.shortcuts import render, redirect
from users.forms import UserRegisterationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}! You are now able to login.')
            return redirect('account:login')
        else:
            messages.warning(request, 'Oops! Please try again')
            return redirect('account:register')
    else:
        messages.success(request, f'Hi! Fill in fields to join')
        form = UserRegisterationForm()

    return render(request, 'users/accounts/register.html', {'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            username = u_form.cleaned_data.get('username')
            u_form.save()
            p_form.save()
            messages.success(request, f"Hello {username}, you're  profile has been update.")
            return redirect('account:profile')
        else:
            messages.success(request, f'Oops! Something went wrong. Please try updating again')
            return redirect('account:profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/accounts/profile.html', context)