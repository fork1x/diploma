from django.shortcuts import redirect, render
from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm
from django.contrib import auth, messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, 'Вы успешно авторизовались!')
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Home - авторизация', 
        'form': form
    }
    return render(request, 'users/login.html', context)

def registration(request):

    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
                form.save()
                auth.login(request, form.instance) # После регистрации сразу логиним пользователя
                messages.success(request, 'Вы успешно зарегистрировались!')
                return HttpResponseRedirect(reverse('main:index')) # После регестрации пользователь должен же залогиниться
    else:
        form = UserRegistrationForm()


    context = {'title': 'Home - регистрация', 'form': form}
    return render(request, 'users/registration.html', context)

@login_required
def profile(request):

    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль успешно обновлён!')
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = ProfileForm(instance=request.user)


    context = {'title': 'Home - кабинет', 'form': form}
    return render(request, 'users/profile.html', context)

@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'Вы успешно вышли из аккаунта!')
    return redirect(reverse('main:index'))