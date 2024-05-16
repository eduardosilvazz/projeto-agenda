from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth, messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from contact.forms import RegisterForm, RegisterUpdateForm

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado')
            return redirect('contact:login')
    
    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )

@login_required(login_url='contact:login')
def user_update(request):
    if request.method == 'POST':
        form = RegisterUpdateForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('contact:login')  # Redirecionar para a página de login após a atualização bem-sucedida
    else:
        form = RegisterUpdateForm(instance=request.user)
    
    return render(
        request,
        'contact/user_update.html',
        {
            'form': form
        }
    )

def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com sucesso!')
            return redirect('contact:index')
        messages.error(request, 'Login inválido')

    return render(
        request,
        'contact/login.html',
        {
            'form': form
        }
    )

@login_required(login_url='contact:login')
def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')