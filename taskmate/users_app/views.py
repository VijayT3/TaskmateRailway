from django.shortcuts import render, redirect
from .forms import CustomRegisterForm
from django.contrib import messages


def register(request):
    if request.method == "POST":
        register_form = CustomRegisterForm(request.POST)
    #  content in form
        if register_form.is_valid():
            register_form.save()
            messages.success(
                request, ("New User Created Successfully! Login to get started."))
            return redirect('register')
    else:
        register_form = CustomRegisterForm(request.POST)
    return render(request, 'register.html', {'register_form': register_form})
