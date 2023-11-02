from django.template import loader
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.http import HttpResponse
import csv
from .models import Contact


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

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

def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="contacte.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nume', 'Prenume', 'Email', 'Telefon', 'Număr de Persoane', 'Nume Suplimentar', 'Mesaj'])

    contacts = Contact.objects.all()
    for contact in contacts:
        writer.writerow([contact.first_name, contact.last_name, contact.email, contact.phone, contact.num_of_people, contact.additional_name, contact.message])

    return response

