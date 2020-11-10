from django.urls import path
from .views import index, gambit, multipage, amongus, sign_in, register

urlpatterns = [
    path('', index, name='homepage'),
    # path('htmltrain', htmltrain),
    path('gambit', gambit, name='gambit'),
    path('multi_page/<int:page_id>', multipage, name='multipage'),
    path('among_us/<int:page_id>', amongus, name='amongus'),
    path('login', sign_in, name='loginpage'),
    path('register', register, name='register'),
]