from django.shortcuts import render

from friendsalbum2026.photo.models import Photo


# Create your views here.
def login_profile(request):
    return None

def register_profile(request):
    return None

def delete_profile(request, pk):
    return None

def edit_profile(request, pk):
    return None

def details_profile(request, pk):
    return None

def visitors_profile(request):
    #return None
    photo = Photo.objects.last()

    context = {
        'photo': photo
    }

    return render(request, 'accounts/visitors_page.html', context)