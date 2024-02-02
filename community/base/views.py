from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')  # Redirect to a success page
    else:
        form = CustomUserCreationForm()
    return render(request, 'base/register.html', {'form': form})

def registration_success(request):
    return render(request, 'base/success.html')


# Create your views here.
