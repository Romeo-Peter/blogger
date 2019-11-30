from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from users.forms import UserRegisterationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Accounted created for {username}!')
            return redirect('blog:blog_home')
    else:
        form = UserRegisterationForm()
        messages.warning(request, f'Hi guest! Fill in fields to join')

    return render(request, 'users/register.html', {'form':form})
