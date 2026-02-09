
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()


def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('book_list')
	else:
		form = AuthenticationForm()
	return render(request, 'accounts/login.html', {'form': form})

def register_view(request):
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('profile')
	else:
		form = CustomUserCreationForm()
	return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile_view(request):
	return render(request, 'accounts/profile.html', {'user': request.user})
