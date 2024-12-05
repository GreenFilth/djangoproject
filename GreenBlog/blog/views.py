
from django.shortcuts import render
from .models import Post, postComment
# Create your views here.


MENU = {"главная": '/', 'о нас': '/about', 'блог': '/posts', 'отзывы': '/addcomment'}


def posts_page(request):
    posts = Post.objects.all()
    title = 'Блог'
    data = {'menu': MENU, 'title': title, 'posts': posts}
    return render(request, './posts.html', context=data)


def comment_page(request):
    posts = Post.objects.values('name','id')
    title = 'Оставить комментарий'
    data = {'menu': MENU, 'title': title, 'posts': posts}
    return render(request, './addcomment.html', context=data)



def thx_page(request):
    user_name = request.POST['user_name']
    comment = request.POST['comment']
    post = Post.objects.get(pk=request.POST['post'])
    postComment.objects.create(user_name=user_name, comment=comment, post=post)
    title = 'Комментарий оставлен'
    data = {'menu': MENU, 'title': title, 'user_name': user_name}
    return render(request, './thxxpage.html', context=data)