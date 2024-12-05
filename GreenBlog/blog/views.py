from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Review
# Create your views here.


MENU = {"главная": '/', 'о нас': '/about', 'блог': '/posts', 'отзывы': '/addcomment'}


def posts_page(request):
    reviews = Review.objects.all()
    title = 'Блог'
    data = {'menu': MENU, 'title': title, 'reviews': reviews}
    return render(request, './posts.html', context=data)


def comment_page(request):
    reviews = Review.objects.all()
    title = 'Оставить комментарий'
    data = {'menu': MENU, 'title': title, 'reviews': reviews}
    return render(request, './addcomment.html', context=data)