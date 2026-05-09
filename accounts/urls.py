from django.urls import path
from . import views

urlpatterns = [

    path('signup/', views.signup),

    path('login/', views.custom_login),

    path('logout/', views.custom_logout),

    path('profile/', views.profile),

]