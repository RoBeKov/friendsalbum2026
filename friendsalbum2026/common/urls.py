from django.urls import path

from friendsalbum2026.common import views

urlpatterns = [
    path('', views.home_page, name='home_page')
]
#from django.urls import path
#from django.http import HttpResponse

#def test(request):
    #return HttpResponse("It works")

#urlpatterns = [
    #path('', test),
#]