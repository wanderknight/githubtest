from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.views.generic import View

from .models import Book


# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class ListView(View):
    def get(self, request, page=1):
        sort = request.GET.get('sort')
        if sort == 'price':
            book_list = Book.objects.order_by('price')
        elif sort == 'douban_score':
            book_list = Book.objects.order_by('-douban_score')
        else:
            sort = 'default'
            book_list = Book.objects.order_by('-id')

        # 对数据进行分页
        paginator = Paginator(book_list, 2)
        # todo fix 分页每页显示数量

        # 获取page 页数字
        try:
            page_number = int(page)
        except Exception as e:
            page_number = 1
        if page > paginator.num_pages:
            page_number = 1

        # 获取第page页的Page实例对象
        page_obj = paginator.get_page(page_number)

        # 1.总页数小于5页，页面上显示所有页码
        # 2.如果当前页是前3页，显示1-5页
        # 3.如果当前页是后3页，显示后5页
        # 4.其他情况，显示当前页的前2页，当前页，当前页的后2页
        num_pages = paginator.num_pages
        if num_pages < 5:
            pages = range(1, num_pages + 1)
        elif page <= 3:
            pages = range(1, 6)
        elif num_pages - page <= 2:
            pages = range(num_pages - 4, num_pages + 1)
        else:
            pages = range(page - 2, page + 3)
        context = {
            'page_obj': page_obj,
            'pages': pages,
            'sort': sort
        }
        return render(request, 'book_list.html', context)


class DetailView(View):
    def get(self, request, book_id):
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return redirect(reverse('book:list1'))
        return render(request, 'book_detail.html', {'book': book})
