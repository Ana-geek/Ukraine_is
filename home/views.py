from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'home/index.html')


# def htmltrain(request):
#     # return render(request, 'home/html-train.html')
#     return render(request, 'base.html')


def gambit(request):
    return render(request, 'home/gambit.html')

