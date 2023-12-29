from django.contrib import admin
from django.urls import path
from recipes.views import home, sobre, contato

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', home),
    path('contato/', contato),
    path('sobre/', sobre),
]