from django.http import HttpResponse


def main(request):
    return HttpResponse("<h1>Hello, user!</h1>")


def about(request):
    return HttpResponse("<h1>ABOUT</h1>")


def post(request):
    return HttpResponse("<h1>POST</h1>")
