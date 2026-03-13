from django.http import HttpResponse
from django.shortcuts import render, redirect

from friendsalbum2026.photo.forms import PhotoForm


# Create your views here.
def add_photo(request):
    #return None
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home_page')

    else:
        form = PhotoForm()

    context = {
        'form': form
    }

    return render(request, 'photo/photo_add_page.html', context)

def details_photo(request):
    return HttpResponse("<h2>Страницата се работи</h2>")

def edit_photo(request):
    return HttpResponse("<h2>Страницата се работи</h2>")