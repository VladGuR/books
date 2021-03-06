from django.urls import re_path, path
import mainapp.views as main

app_name = 'mainapp'

urlpatterns = [
    re_path('genres/$', main.genres, name='genres'),
    re_path('genre/(?P<genre>.*\s*)/$', main.genre, name='genre'),
    re_path('top/$', main.top, name='top'),
    re_path('pop/$', main.pop, name='pop'),
    re_path('new/$', main.new, name='new'),
    re_path('search/$', main.search, name='search'),
    re_path('book/(?P<book>.*\s*)/$', main.book, name='book'),
]
