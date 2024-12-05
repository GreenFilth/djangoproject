from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', posts_page),
    path('addcomment', comment_page),

]
