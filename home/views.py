from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')


# def htmltrain(request):
#     # return render(request, 'home/html-train.html')
#     return render(request, 'base.html')


def gambit(request):
    return render(request, 'home/gambit.html')


def multipage(request, page_id: int):
    print(page_id)
    data = {
        'page__id': page_id,
        'text': 'hello to you',
        'animals': ['cat', 'dog', 'bat', 'owl'],
        'range': range(10)
    }
    return render(request, 'home/multi-value-page.html', context=data)


def amongus(request, page_id: int):
    print(page_id)
    data = {
        'page__id': page_id,
        'text': 'well, well...',
        'roles': ['crew', 'impostor', 'crew', 'impostor', 'crew', 'crew', 'crew', 'impostor', 'crew', 'crew'],
        'players': range(1, 11)
    }
    return render(request, 'home/among_us.html', context=data)


def sign_in(request):
    return render(request, 'home/login.html')


def register(request):
    return render(request, 'home/register.html')