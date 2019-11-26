from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Accounted created for {username}!')
            return redirect('blog_home')
    else:
        form = UserCreationForm()
        messages.warning(request, f'Hi guest! Fill in fields to join')

    return render(request, 'users/register.html', {'form':form})
