from django.shortcuts import render,redirect
from .models import Event
from .forms import BookingForm


# Create your views here.

def Index(request):
    return render(request, 'Index.html')


def About(request):
    return render(request, 'About.html')


def Contact(request):
    return render(request, 'Contact.html')


def Booking(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = BookingForm()
    dict_form = {
        'form': form
    }

    return render(request, 'Booking.html',dict_form)


def Events(request):
    dict_eve = {
        'eve': Event.objects.all()
    }
    return render(request, 'Events.html', dict_eve)
