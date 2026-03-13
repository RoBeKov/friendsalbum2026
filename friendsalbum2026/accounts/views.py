from django.http import HttpResponse
from django.shortcuts import render

from friendsalbum2026.photo.models import Photo


# Create your views here.
def login_profile(request):
    return HttpResponse("<h2>Страницата се работи</h2>")

def register_profile(request):
    return HttpResponse("<h2>Страницата се работи</h2>")

def delete_profile(request, pk):
    return None

def edit_profile(request, pk):
    return None

def details_profile(request, pk):
    return None

def visitors_profile(request):
    #return None
    photos = Photo.objects.all().order_by('-date_of_publication')

    context = {
        'photos': photos
    }

    return render(request, 'accounts/visitors_page.html', context)