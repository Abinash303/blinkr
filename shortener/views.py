import logging
logger = logging.getLogger(__name__)
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import URL
from .forms import URLForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

@login_required
def dashboard(request):
    urls = URL.objects.filter(user=request.user)
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            url.user = request.user
            url.save()
            return redirect('dashboard')
    else:
        form = URLForm()
    return render(request, 'dashboard.html', {'form': form, 'urls': urls})

def redirect_short(request, code):
    url = get_object_or_404(URL, short_code=code)
    url.click_count += 1
    url.save()
    logger.info(f"CLICK COUNT UPDATED: {url.short_code} -> {url.click_count}")
    return redirect(url.original_url)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})