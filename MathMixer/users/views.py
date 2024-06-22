from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login
from django.urls import reverse
from django.views.generic import TemplateView
from .forms import LoginUserForm, RegisterUserForm
from django.contrib.auth.views import LoginView
def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.avatar = 'static/avatars/default_avatar.png'
            user.save()
            login(request, user)
            return redirect('users:home')
        else:
            print(form.errors)
            print("Form is not valid")
    else:
        form = RegisterUserForm()
    return render(request, 'register.html', {'form': form})

def home(request):
    return render(request, 'home.html')

class LoginUsersView(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['date_joined'] = user.date_joined
        return context
def trainers_redirect(request):
    if request.user.is_authenticated:
        return redirect(reverse('main:trainersN'))
    else:
        return redirect(reverse('users:login'))
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Профайл успешно обновлен")
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'edit_profile.html')