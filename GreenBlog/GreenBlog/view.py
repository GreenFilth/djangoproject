from django.http import HttpResponse
from django.shortcuts import render

MENU = {"главная": '/', 'о нас': '/about', 'блог': '/posts'}


def main(request):
    title = 'Главная страница'
    data = {'menu': MENU, 'title': title}
    return render(request, './index.html', context=data)


def about_page(request):
    title = 'о нас'
    data = {'menu': MENU, 'title': title}
    return render(request, './about.html', context=data)


