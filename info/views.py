from django.shortcuts import render, HttpResponseRedirect
from django.http import request, HttpResponse
from .models import Profile, ProfileForm


# Create your views here.


def index(request):
    if request.method == 'POST':
        # creating a form instance
        form = ProfileForm(request.POST)
        # form validity check
        if form.is_valid():
            form.save()

            return HttpResponse("<h3>record added succesfully <h3>")
    else:
        form = ProfileForm()
        profile = Profile.get_profile()
        context = {
            'profile': profile,
            'form': form,
        }
        return render(request, 'info/index.html', context)


# this is displayed as the first page of the site


def first(request):
    return render(request, 'info/first.html')