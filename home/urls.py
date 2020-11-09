from django.urls import path
from .views import index, gambit

urlpatterns = [
    path('', index),
    # path('htmltrain', htmltrain),
    # path ('about', about)
    path('gambit', gambit)
]