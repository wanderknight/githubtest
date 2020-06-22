from django.urls import path
from .views import IndexView, ListView, DetailView

urlpatterns = [
    path('index', IndexView.as_view(), name='index'),
    path('list/<int:page>', ListView.as_view(), name='list'),
    path('list', ListView.as_view(), name='list1'),
    path('detail/<int:book_id>', DetailView.as_view(), name='detail'),
    path('', IndexView.as_view(), name='index'),
]
