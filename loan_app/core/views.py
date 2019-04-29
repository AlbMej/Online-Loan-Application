from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from .forms import AddressForm, CustomFieldForm
# Create your views here.

def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })

class LoanForm(LoginRequiredMixin, FormView):
    form_class = CustomFieldForm
    success_url = reverse_lazy('success')
    template_name = 'form.html'

class SuccessView(TemplateView):
    template_name = 'success.html'