from django.template import loader
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.http import HttpResponse
import csv



def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

# Create your views here.
# views.py


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # save to bd
            return redirect('home_success')  # redirect success

    else:
        form = ContactForm()

    return render(request, 'home.html', {'form': form})



def home_success(request):
    return render(request, 'home_success.html')


