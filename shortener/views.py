from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import URL
from .forms import URLForm

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
    return redirect(url.original_url)
