from django.urls import path, include

from friendsalbum2026.accounts import views

urlpatterns = [
    path('login/', views.login_profile, name='login_profile'),
    path('register/', views.register_profile, name='register_profile'),
    path('visitors/', views.visitors_profile, name='visitors_profile'),
    path('profile/<int:pk>/', include([
        path('', views.details_profile, name='details_profile'),
        path('edit/', views.edit_profile, name='edit_profile'),
        path('delete/', views.delete_profile, name='delete_profile')
    ]))

]